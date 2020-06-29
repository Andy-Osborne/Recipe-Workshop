import os
from flask import Flask, render_template, url_for, redirect, request, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from usercreation import UserRegistration, UserLogin, UserUpdate
from passlib.hash import pbkdf2_sha256

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Global Variables

recipe = mongo.db.recipe
user = mongo.db.users

# Handles the logic for the front page and displays the highest rated recipe & 6 most recently added.

@app.route("/")
def index():

    highest_rated = recipe.find({"likes":{"$gt": 0}}).sort("likes", -1).limit(1)
    recent_recipes = recipe.find().sort("submitted", -1).limit(8)

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
        recipe_name = req["recipe_name"]
        course = req["dish_type"]
        description = req["description"]
        image_url = req["recipe_image"]
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

        new_recipe = {
            "recipe_author": session["username"],
            "recipe_name": recipe_name,
            "recipe_course": course,
            "recipe_description" : description,
            "recipe_image" : image_url,
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

    return render_template("public/create_recipe.html")

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
        recipe_name = req["recipe_name"]
        course = req["dish_type"]
        description = req["description"]
        image_url = req["recipe_image"]
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

        recipe.update_one({"_id":ObjectId(recipe_id)},
        {
            "$set": {
                "recipe_name": recipe_name,
                "recipe_course": course,
                "recipe_description" : description,
                "recipe_image" : image_url,
                "prep_time": int(prep_time),
                "cooking_time": int(cook_time),
                "effort": effort,
                "servings": int(servings),
                "steps": steps_list,
                "ingredients": ingredient_list
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

    recipe.delete_one({"_id":ObjectId(recipe_id)})
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
                return redirect("/")

            elif username_search > 0:
                flash(f"Username already taken. Please choose a different username.", "error_username")
                return redirect(request.url)

            elif email_search > 0:
                flash(f"Email already in use. Please use login.", "error_email")
                return redirect(request.url)
        else:
            return render_template("public/register.html", title="Register", form=form)  
            
    elif request.method == "GET":
        return render_template("public/register.html", title="Register", form=form)   
        
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

            return render_template("public/login.html", title="Login", form=form)

        else:
            return render_template("public/login.html", title="Login", form=form)   
           
    elif request.method == "GET":
        return render_template("public/login.html", title="Login", form=form)   

# Handles logging out user by clearing session data.

@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    user_profile = user.find_one({"username": username})
    session_user = session["username"]
    
    return render_template("public/profile.html", username=user_profile, recipes=mongo.db.recipe.find(), session_user=session_user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("public/404.html"), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)

