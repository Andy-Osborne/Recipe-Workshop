import os
from flask import (Flask, render_template,
                   url_for, redirect, request, flash, session, jsonify)
from flask_pymongo import PyMongo
from flask_paginate import Pagination, get_page_parameter
from bson.objectid import ObjectId
from datetime import datetime
from usercreation import UserRegistration, UserLogin
from passlib.hash import pbkdf2_sha256 as p256
import cloudinary
import cloudinary.uploader
import cloudinary.api

if os.path.exists('env.py'):
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
newsletter = mongo.db.newsletter
cloud = cloudinary.uploader

# Handles landing page logic


@app.route("/")
def index():

    # Finds most liked recipe and 8 most recent recipes

    highest_rated = recipe.find({"likes":
                                {"$gt": 0}}).sort("likes", -1).limit(1)
    recent_recipes = recipe.find().sort("submitted", -1).limit(8)

    """
    Below relates to the newsletter sign-up. If there is a username in
    session and its in newsletter collection, it assigns it to a variable.
    If either are conditions are false, variable is an empty string.
    """

    if "username" in session:
        newsletter_check = newsletter.find_one({
            "username": session["username"]})

        if newsletter_check is None:
            signups = ""
        else:
            signups = session["username"]
    else:
        signups = ""

    return render_template("index.html", favourite=list(highest_rated),
                           recent=list(recent_recipes), signups=signups,
                           page="index")

# The below is the view for the search bars.


@app.route("/search", methods=["POST"])
def get_search():
    return redirect(url_for("search_recipes",
                            search_term=request.form.get("search_field")))

# The below generates the search page based on the search term.


@app.route("/search/<search_term>")
def search_recipes(search_term):

    # The below creates the index for the text search and defines the fields.

    recipe.create_index([
        ("recipe_name", "text"),
        ("ingredients", "text"),
        ("recipe_course", "text"),
        ("recipe_description", "text"),
        ("recipe_author", "text")
    ])

    # Below is used for flask-paginate

    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    # Restricts the amount of results per page

    per_page = 4

    """
    This uses the mongodb text search functionality, sorts the results by it's
    metascore, skips a X results based on page variable less 1, and
    limits the returned in results on each page based on the variable per_page
    """

    search_result = recipe.find({"$text": {"$search": search_term}},
                                {'score': {'$meta': 'textScore'}}).sort([
                                    ('score', {'$meta': 'textScore'})]).skip(
                                        (page - 1) * per_page).limit(per_page)

    # Records the amount of items that match the search criteria

    search_count = recipe.count_documents({"$text": {"$search": search_term}})

    pagination = Pagination(page=page, per_page=per_page, total=search_count,
                            search=search, record_name='search_result',
                            css_framework='bootstrap4')

    return render_template('search.html', search_term=search_term,
                           search_result=search_result, count=search_count,
                           pagination=pagination)

# Handles logic for displaying recipes


@app.route("/recipe/<recipe_id>/<recipe_name>")
def get_recipe(recipe_id, recipe_name):
    recipe_view = recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe_view)

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

        """
        The below uses the helper functions to create an populate the list for
        steps and ingredients based on results from recipe form.
        """

        recipe_ingredients(req)
        recipe_steps(req)

        # Below is cloudinary helper function to upload recipe image

        upload_image(image, "recipe")

        new_recipe = {
            "recipe_author": session["username"],
            "recipe_name": recipe_name,
            "recipe_course": course,
            "recipe_description": description,
            "recipe_image": image_url,
            "image_id": image_id,
            "prep_time": int(prep_time),
            "cooking_time": int(cook_time),
            "effort": effort,
            "servings": int(servings),
            "steps": steps_list,
            "ingredients": ingredient_list,
            "submitted": datetime.now(),
            "likes": 0,
            "liked_by": []
        }

        recipe.insert_one(new_recipe)
        return redirect("/")

    return render_template("create_recipe.html", page="add_recipe")

# Displays the manage recipe page to user


@app.route("/manage/<recipe_id>")
def manage_recipe(recipe_id):

    edit_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})

    # Prevents user who is not recipe owner from editing recipe

    if session["username"] != edit_recipe["recipe_author"]:
        return redirect("/")

    return render_template("manage_recipe.html", recipe=edit_recipe)

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

        # Helper functions to populate recipe and steps list

        recipe_ingredients(req)
        recipe_steps(req)

        recipe.update_one({"_id": ObjectId(recipe_id)},
                          {
                            "$set": {
                                "recipe_name": recipe_name,
                                "recipe_course": course,
                                "recipe_description": description,
                                "prep_time": int(prep_time),
                                "cooking_time": int(cook_time),
                                "effort": effort,
                                "servings": int(servings),
                                "steps": steps_list,
                                "ingredients": ingredient_list
                            }
            })

        if reqf:

            # The below gets the image public id from recipe

            id_find = recipe.find_one({"_id": ObjectId(recipe_id)},
                                      {"image_id": 1})
            public_id = id_find["image_id"]

            # The below deletes the recipe image from cloudinary

            cloud.destroy(public_id)

            image = reqf["recipe_image"]

            # Below is cloudinary helper function to upload new image

            upload_image(image, "recipe")

            recipe.update_one({"_id": ObjectId(recipe_id)},
                              {
                                "$set": {
                                    "recipe_image": image_url,
                                    "image_id": image_id
                                }
                            })

    return redirect(url_for("get_recipe", recipe_id=recipe_id,
                            recipe_name=recipe_name))

# Handles logic for deleting a recipe


@app.route("/delete/<recipe_id>")
def delete_recipe(recipe_id):

    recipe_check = recipe.find_one({"_id": ObjectId(recipe_id)})

    # Prevents user who is not recipe owner from deleting recipe

    if session["username"] != recipe_check["recipe_author"]:
        return redirect("/")

    else:
        recipe.delete_one({"_id": ObjectId(recipe_id)})

        # The below deletes the recipe image from cloudinary

        public_id = recipe_check["image_id"]
        cloud.destroy(public_id)

    return redirect(url_for("profile", username=session["username"]))


# Handles the logic of a user liking or removing their like from a recipe

@app.route("/like/<recipe_id>", methods=["GET", "POST"])
def like(recipe_id):
    find_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})

    """
    The below checks if username is in the recipe liked_by field. If it is
    it decrements the likes of recipe by 1 and removes username from field.
    If the username is not, it increases likes by 1 and adds username to field.
    """

    if session["username"] not in find_recipe["liked_by"]:
        recipe.update_one(
            {'_id': ObjectId(recipe_id)},
            {
                "$inc": {"likes": 1},
                "$push": {"liked_by": session["username"]}
            })
        new_like = recipe.find_one({"_id": ObjectId(recipe_id)})["likes"]
        return jsonify({'add': new_like})
    else:
        recipe.update_one(
            {'_id': ObjectId(recipe_id)},
            {
                "$inc": {"likes": -1},
                "$pull": {"liked_by": session["username"]}
            })
        new_like = recipe.find_one({"_id": ObjectId(recipe_id)})["likes"]
        return jsonify({'remove': new_like})


# Handles the user registration logic

@app.route('/register', methods=["GET", "POST"])
def user_registration():
    form = UserRegistration()

    if request.method == "POST" and form.validate_on_submit():
        req = request.form

        # Looks for username and email in current user collection

        username_search = user.count_documents(
            {"username": req["username"]})

        email_search = user.count_documents({"email": req["email"]})

        # If email and username count is 0 it creates a new user record

        if email_search <= 0 and username_search <= 0:
            new_user = {
                "username": req["username"],
                "email": req["email"],
                "password": p256.hash(req["password"])
                }
            user.insert_one(new_user)
            session['username'] = req["username"]
            return redirect(url_for("profile",
                                    username=session['username']))

        # If username / email count is greater than 0, message is shown to user

        elif username_search > 0:
            flash(u"Username already taken. Choose a different username.",
                  "error_username")
            return redirect(request.url)

        elif email_search > 0:
            flash(u"Email already in use. Please use login.",
                  "error_email")
            return redirect(request.url)

    return render_template("register.html", form=form, page="register")

# Handles the user login logic


@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserLogin()

    if request.method == "POST" and form.validate_on_submit():

        req = request.form
        email = req["email"]
        password = req["password"]

        existing_user = user.find_one({"email": email})

        # Checks to see if user is in database - if true, checks password

        if existing_user is not None:
            c_password = existing_user["password"]

            # Verifies entered password against user password field.

            if p256.verify(password, c_password):

                # If passwords match, session variable assigned username

                session["username"] = existing_user["username"]
                return redirect(
                                url_for("profile", username=session['username']
                                        ))
            else:
                flash(u"Incorrect e-mail/password combination.",
                      "error")
                return redirect(request.url)
        else:
            flash(u"Incorrect e-mail/password combination.",
                  "error")
            return redirect(request.url)

    return render_template("login.html", form=form, page="login")

# Handles logging out user by clearing session data.


@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.clear()
    return redirect(url_for("index"))

# Handles the logic of generating user profile and displaying recipes


@app.route("/profile/<username>", methods=["GET"])
def profile(username):
    user_profile = user.find_one({"username": username})
    recipe_count = recipe.count_documents({"recipe_author": username})

    return render_template("profile.html", username=user_profile,
                           recipes=recipe.find(), recipe_count=recipe_count,
                           page="profile")

# Handles user adding their profile information.


@app.route("/profile/update/<username>", methods=["POST", "GET"])
def update_profile(username):

    user_profile = user.find_one({"username": username})

    # Prevents user who is not profile owner from updating it

    if session["username"] != user_profile["username"]:
        return redirect("/")

    if request.method == "POST":
        reqf = request.form

        profile_image = request.files["profile-image"]

        # The below uses the Cloudinary Upload Code helper Function

        upload_image(profile_image, "profile")

        user.update_one({"_id": ObjectId(user_profile["_id"])},
                        {
                            "$set": {
                                "profile_image": image_url,
                                "profile_image_id": image_id,
                                "profile_description": (
                                    reqf["profile-description"])
                            }
                        })

    return redirect(request.referrer)

# Handles the logic for updating a users account information


@app.route("/profile/account_management", methods=["POST"])
def update_account():
    req = request.form

    user_id = req["user_id"]
    n_email = req["email"]
    password = req["password"]
    n_password = ""

    # Checks to see if a new password has been submitted

    if "new-password" in req:
        n_password = req["new-password"]
        c_password = req["conf-password"]

    user_profile = user.find_one({"_id": ObjectId(user_id)})
    u_pass = user_profile["password"]
    u_email = user_profile["email"]

    # Check to see if no new pasword and email has not changed

    if u_email == n_email and n_password == "":
        return jsonify(
            {'error': "Account not updated - no new information given."})

    # Verifies the password entered matches the one registered

    if p256.verify(password, u_pass):

        # Checks to see if a new email and pass has been entered

        if u_email != n_email and n_password != "":

            # If new pass and email, checks to see if they match

            if new_pass_check(n_password, c_password):

                # If new pass match then it updates email and pass
                email_update(user_id, n_email)
                password_update(user_id, n_password)
                return jsonify(
                    {'success': "Account successfully updated!"})
            else:
                return jsonify(
                    {'error': "New passwords do not match."})

        # If no new password is entered, it runs the update email function

        elif u_email != n_email:

            email_update(user_id, n_email)
            return jsonify({'success': "Email successfully updated!"})

        # If no new email entered, checks to see if new password was entered

        elif new_pass_check(n_password, c_password):

            # If new pass match then it updates pass
            password_update(user_id, n_password)
            return jsonify(
                {'success': "Password successfully updated!"})

        else:
            return jsonify(
                {'error': "New passwords do not match."})

    # If account password does not match. Below is shown to user.

    else:
        return jsonify({'error': "Incorrect current password entered."})


# Below view is for  the privacy page


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

# Below is the logic that handles the newsletter signup


@app.route("/newsletter",  methods=["POST"])
def newsletter_register():

    email = request.form["email"]
    duplicate_search = newsletter.find_one({"email": email})

    # Checks to see if a username is in session then assigns to variable

    if "username" in session:
        username = session["username"]
    else:
        username = ""

    # Checks to see if email is already in newsletter collection

    if not duplicate_search:

        # Checks to see if username variable is empty and only inserts email

        if username == "":
            new_signup = {
                "email": email
            }

            newsletter.insert_one(new_signup)
            return jsonify(
                {'success': "Thank you! You've joined our newsletter list."})

        # If there is info in username variable, inserts email and username

        else:
            new_signup = {
                "email": email,
                "username": username
            }

            newsletter.insert_one(new_signup)
            return jsonify(
                {'success': "Thank you! You've joined our newsletter list."})

    else:

        # Adds username to collection if email is in it and username is not

        if username:
            newsletter.update_one({"_id": ObjectId(duplicate_search["_id"])},
                                  {
                                        "$set": {
                                            "username": username
                                        }
                                    })

            return jsonify(
                {'error': "Looks like you're already in our newsletter list!"})

        else:

            # If no given username & email is already in newsletter collection

            return jsonify(
                {'error': "Looks like you're already in our newsletter list!"})

# Below code taken from a rip tutorial and edited to only show the DD/MM/YYYY


@app.template_filter('formatdatetime')
def format_datetime(value, format="%d %b %Y"):
    if value is None:
        return ""
    return value.strftime(format)

# Below is the logic for dealing with 404 errors


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Recipe Helper Functions

# Takes the ingredients from the recipe form and assigns to a list

def recipe_ingredients(req):
    global ingredient_list
    ingredient_list = []

    for key in req.keys():
        if key == "ingredients":
            for value in req.getlist(key):
                ingredient_list.append(value)


# Takes the steps from the recipe form and assigns to to a list

def recipe_steps(req):
    global steps_list
    steps_list = []

    for key in req.keys():
        if key == "step":
            for value in req.getlist(key):
                steps_list.append(value)


# Cloudinary Upload Code

"""
This takes in the variable which has been assigned the request file,
it then uploads the image - resizes and compresses image.
The folder_string variable is the name of the folder to be used in
cloudinary's website.

The variables used in there are global so they can be accessed by the
updating form.
"""


def upload_image(vairable, folder_string):
    global uploaded_image
    global image_url
    global image_id
    uploaded_image = cloud.upload(vairable, width=500, height=500,
                                  quality="auto",
                                  folder=f"Recipe_Workshop/{folder_string}/")

    image_url = uploaded_image.get("secure_url")
    image_id = uploaded_image.get("public_id")


# Account Update Helper Functions


def new_pass_check(new, conf):
    if new == conf:
        return True
    else:
        return False


def email_update(user_id, new_email):
    user.update_one({"_id": ObjectId(user_id)},
                    {
                        "$set": {
                                "email": new_email,
                        }
                    })


def password_update(user_id, new_password):
    user.update_one({"_id": ObjectId(user_id)},
                    {
                        "$set": {
                                "password": p256.hash(new_password)
                        }
                    })


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
