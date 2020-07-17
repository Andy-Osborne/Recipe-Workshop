import os
from flask import Flask, render_template, url_for, redirect, request, flash, session, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from usercreation import UserRegistration, UserLogin
from passlib.hash import pbkdf2_sha256
import cloudinary
import cloudinary.uploader
import cloudinary.api

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DB")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config["CLOUDINARY_URL"] = os.environ.get("CLOUDINARY_URL")

mongo = PyMongo(app)

# Global Variables

recipe = mongo.db.recipe
user = mongo.db.users

# Handles the logic for the front page and displays the highest rated recipe & 6 most recently added.

@app.route("/")
def index():

    highest_rated = recipe.find({"likes":{"$gt": 0}}).sort("likes", -1).limit(1)
    recent_recipes = recipe.find().sort("submitted", 1).limit(8)

    return render_template("public/index.html", favourite=list(highest_rated), recent=list(recent_recipes))


@app.route("/search", methods=["POST"])
def get_search():
    return redirect(url_for("search_recipes", search_term=request.form.get("search_field")))


@app.route("/search/<search_term>")
def search_recipes(search_term):
    
    # The below creates the index for the text search and defines the fields to use.

    recipe.create_index([
        ("recipe_name", "text"),
        ("ingredients", "text"),
        ("recipe_course", "text"),
        ("recipe_description", "text"),
        ("recipe_author", "text")
    ])

    # The below uses the text search functionality, and then sorts the results by it's metascore

    search_result = recipe.find({"$text": {"$search": search_term}}, 
    {'score': {'$meta': 'textScore'}}).sort([('score', {'$meta': 'textScore'})])

    search_count = recipe.count_documents({"$text": {"$search": search_term}})

    return render_template('public/search.html', search_term=search_term, search_result=search_result, count=search_count)    


@app.route("/recipe/<recipe_id>/<recipe_name>")
def get_recipe(recipe_id, recipe_name):
    recipe_view = recipe.find_one({"_id":ObjectId(recipe_id)})
    return render_template("public/recipe.html", recipe=recipe_view)

# Handles the logic for adding a recipe to database.

@app.route("/create_recipe", methods=["GET", "POST"])
def add_recipe():

    if request.method == "POST":
        req = request.form
        reqf = request.files

        recipe_name = req["recipe_name"]
        course = req["dish_type"]
        description = req["description"]
        image = reqf["recipe_image"]
        prep_time = req["preparation_time"]
        cook_time = req["cooking_time"]
        effort = req["effort"]
        servings = req["servings"]

        ingredient_list = []
        steps_list = []

        """The below for loop iterates over the form data and as the fields for 
        ingredients and steps are dynamic, they will vary according the users needs, and it will 
        add each corresponding value to the associated list which can then be submitted to the database."""

        for key in req.keys():
            if key == "ingredients":
                for value in req.getlist(key):
                    ingredient_list.append(value)
            elif key == "step":
                for value in req.getlist(key):
                    steps_list.append(value)

        # Cloudinary Image Upload Code

        uploaded_image = cloudinary.uploader.upload(image, width=800, quality="auto", 
            folder="Recipe_Workshop/recipe/")
        image_url = uploaded_image.get("secure_url")
        image_id = uploaded_image.get("public_id")
        
      
        new_recipe = {
            "recipe_author": session["username"],
            "recipe_name": recipe_name,
            "recipe_course": course,
            "recipe_description" : description,
            "recipe_image" : image_url,
            "image_id": image_id,
            "prep_time": int(prep_time),
            "cooking_time": int(cook_time),
            "effort": effort,
            "servings": int(servings),
            "steps": steps_list,
            "ingredients": ingredient_list,
            "submitted" : datetime.today().strftime('%d-%m-%Y'),
            "likes" : 0,
            "liked_by" : []
        }

        recipe.insert_one(new_recipe)
        return redirect("/")

    return render_template("public/create_recipe.html", page="add_recipe")

# Displays the manage recipe page to user

@app.route("/manage/<recipe_id>")
def manage_recipe(recipe_id):

    edit_recipe = recipe.find_one({"_id":ObjectId(recipe_id)})

    """
    If a user tries to enter the manage screen for a recipe they do not own, they are 
    redirected to the home page
    """

    if session["username"] != edit_recipe["recipe_author"]:
        return redirect("/")
   
    return render_template("public/manage_recipe.html", recipe=edit_recipe)


# Handes the logic of updating a recipe

@app.route("/update/<recipe_id>", methods=["GET", "POST"])
def update_recipe(recipe_id):

    if request.method == "POST":
        req = request.form
        reqf = request.files

        recipe_name = req["recipe_name"]
        course = req["dish_type"]
        description = req["description"]
        prep_time = req["preparation_time"]
        cook_time = req["cooking_time"]
        effort = req["effort"]
        servings = req["servings"]

        ingredient_list = []
        steps_list = []


        for key in req.keys():
            if key == "ingredients":
                for value in req.getlist(key):
                    ingredient_list.append(value)
            elif key == "step":
                for value in req.getlist(key):
                    steps_list.append(value)

        """The below checks to see if there is a file request in the form upload.
            If there is not, it will update the recipe and exclude updating the image.
            If there is, it will delete the old image from cloudinary, upload the new image,
            and assign the new url and public id for the image to the recipe in the database. 
        """

        recipe.update_one({"_id":ObjectId(recipe_id)},
            {
                "$set": {
                    "recipe_name": recipe_name,
                    "recipe_course": course,
                    "recipe_description" : description,
                    "prep_time": int(prep_time),
                    "cooking_time": int(cook_time),
                    "effort": effort,
                    "servings": int(servings),
                    "steps": steps_list,
                    "ingredients": ingredient_list
                }
            })
        
        if reqf:
        
            # The below gets the public id related to the recipe, then deletes image from cloudinary
            
            id_find = recipe.find_one({"_id":ObjectId(recipe_id)},{"image_id":1})
            public_id = id_find["image_id"]
            cloudinary.uploader.destroy(public_id)

            # The below uploads the new recipe image to cloudinary, saves the image URL and public ID

            image = reqf["recipe_image"]
            uploaded_image = cloudinary.uploader.upload(image, width=800, quality="auto", 
                folder="Recipe_Workshop/recipe/")
            image_url = uploaded_image.get("secure_url")
            image_id = uploaded_image.get("public_id")

            recipe.update_one({"_id":ObjectId(recipe_id)},
                {
                    "$set": {
                        "recipe_image" : image_url,
                        "image_id": image_id
                        
                    }
                })


    return redirect(url_for("get_recipe", recipe_id=recipe_id,recipe_name=recipe_name))

@app.route("/delete/<recipe_id>")
def delete_recipe(recipe_id):

    recipe_check = recipe.find_one({"_id":ObjectId(recipe_id)})
    """
    If a user gets hold of the url for deleting the recipe, the below will check to see if
    their logged in session is the same as the recipe author. If it is not, it will redirect
    them to the home screen, otherwise it will allow them to delete the recipe.
    """

    if session["username"] != recipe_check["recipe_author"]:
       return redirect("/")

    else:
        recipe.delete_one({"_id":ObjectId(recipe_id)})
         
         # The below gets the public id related to the recipe, then deletes image from cloudinary
            
        public_id = recipe_check["image_id"]
        cloudinary.uploader.destroy(public_id)

    return redirect(url_for("profile", username=session["username"]))


# Handles the logic of a user liking or removing their like from a recipe

@app.route("/like/<user_name>/<recipe_id>", methods=["GET", "POST"])
def like(recipe_id, user_name):
    find_recipe = recipe.find_one({"_id":ObjectId(recipe_id)})

    """The below checks to see if the user who likes the recipe is already in the liked by
    field within the recipes document. If the user is not, then it increments the likes by 1
    and adds the username to liked_by. If the user is already in there, then it treats it as 
    if the user is unliking it and removes their name and decrements the count by 1."""

    if user_name not in find_recipe["liked_by"]:
        recipe.update(
            {'_id': ObjectId(recipe_id)},
            {
                "$inc": {"likes": 1},
                "$push" : {"liked_by": user_name}
        })
    else:
        recipe.update(
            {'_id': ObjectId(recipe_id)},
            {
                "$inc": {"likes": -1},
                "$pull" : {"liked_by": user_name}
        })

    return redirect(request.referrer)

#H Handles the user registration logic

@app.route('/register', methods=["GET", "POST"])
def user_registration():
    form = UserRegistration()

    if request.method == "POST":
        if form.validate_on_submit():
            req = request.form

            """ The username and email search checks the user colllection in the database and 
            counts the amount of times it appears. This is then used in the if statement when
            registering a new user. If the email count is greater than 0, it means that the user
            already has an account and likewise, if the username count is greater than 0 then the
            name has already been taken."""

            username_search = user.count_documents({"username": req["username"]})
            email_search = user.count_documents({"email": req["email"]})

            if email_search <= 0 and username_search <= 0:
                new_user = {
                    "username" : req["username"],
                    "email" : req["email"],
                    "password" : pbkdf2_sha256.hash(req["password"])
                    }    
                user.insert_one(new_user)
                session['username'] =  req["username"]
                return redirect(url_for("profile", username=session['username']))

            elif username_search > 0:
                flash(f"Username already taken. Please choose a different username.", "error_username")
                return redirect(request.url)

            elif email_search > 0:
                flash(f"Email already in use. Please use login.", "error_email")
                return redirect(request.url) 
            
    return render_template("public/register.html", title="Register", form=form, page="register")   
        
# Handles the user login logic

@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserLogin()

    if request.method == "POST":
        if form.validate_on_submit():
            req = request.form
            existing_user = user.find_one({"email": req["email"]})

            if existing_user:
                for fields in existing_user.items():
                    if fields[0] == "username":
                        session_username = fields[1]
                    if fields[0] == "password":
                        if pbkdf2_sha256.verify(req["password"], fields[1]):
                            session['username'] =  session_username
                            return redirect(url_for("profile", username=session['username']))
                        else:
                            flash(f"Incorrect e-mail/password combination. Please try again", "error")
                            session_username = None
                            return redirect(request.url)
            else:
                flash(f"Incorrect e-mail/password combination. Please try again", "error")
                return redirect(request.url)
          
    return render_template("public/login.html", title="Login", form=form, page="login")   

# Handles logging out user by clearing session data.

@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    user_profile = user.find_one({"username": username})
    
    return render_template("public/profile.html", username=user_profile, recipes=mongo.db.recipe.find(), page="profile")

# Handles user creating their profile information.

@app.route("/profile/update/<username>", methods=["POST", "GET"])
def update_profile(username):
    
    user_profile = user.find_one({"username": username})

    if session["username"] != user_profile["username"]:
        return redirect("/")

    if request.method == "POST":
        
        # Cloudinary Image Upload Code

        profile_image = request.files["profile-image"]

        uploaded_profile_image = cloudinary.uploader.upload(profile_image, width=800, quality="auto", 
            folder="Recipe_Workshop/profile/")
        profile_image_url = uploaded_profile_image.get("secure_url")
        profile_image_id = uploaded_profile_image.get("public_id")

        user.update_one({"_id":ObjectId(user_profile["_id"])},
        {
            "$set": {
                "profile_image": profile_image_url,
                "profile_image_id" : profile_image_id, 
                "profile_description": request.form["profile-description"]
            }
        })

    return redirect(request.referrer)

# Handles the logic for updating a users account information

@app.route("/profile/account_management", methods=["POST"])
def update_account():
    req = request.form

    user_id = req["user_id"]
    new_email = req["email"]
    password = req["password"]
    new_password = ""

    for keys in req.items():
        if keys[0] == "new-password":
            new_password = req["new-password"]
        if keys[0] == "conf-password":
            conf_password = req["conf-password"]


    user_profile = user.find_one({"_id":ObjectId(user_id)})

    # Check to see if no new pasword has been submitted and email has not changed

    if new_password == "" and new_email == user_profile["email"]:
        return jsonify({ 'error': "No new information has been provided. Account not updated." })

    # If the above is false then the below will update account

    if pbkdf2_sha256.verify(password, user_profile["password"]):

        if new_email != user_profile["email"]:
            if new_password != "":
                if new_password == conf_password:
                    email_update(user_id, new_email)
                    password_update(user_id, new_password)
                    return jsonify({ 'success': "Account successfully updated!" })
                else:
                    return jsonify({ 'error': "New password and confirmation password do not match." })
            else:
                email_update(user_id, new_email)
                return jsonify({ 'success': "Email successfully updated!" })
        
        elif new_password != "":
            if new_password == conf_password:
                password_update(user_id, new_password)
                return jsonify({ 'success': "Password successfully updated!" })

            else:
                return jsonify({ 'error': "New password and confirmation password do not match." })
    
    else:
        return jsonify({ 'error': "Incorrect current password entered." })       

    return redirect(request.referrer)
        
# Account Update Functions

def email_update(user_id, new_email):
    user.update_one({"_id":ObjectId(user_id)},
        {
            "$set": {
            "email": new_email,
            }
        })


def password_update(user_id, new_password):
    user.update_one({"_id":ObjectId(user_id)},
        {
            "$set": {
            "password" : pbkdf2_sha256.hash(new_password)
            }
        })


@app.errorhandler(404)
def page_not_found(e):
    return render_template("public/404.html"), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)

