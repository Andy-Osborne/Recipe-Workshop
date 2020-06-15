import os
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from usercreation import UserRegistration, UserLogin
from passlib.hash import pbkdf2_sha256

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("NONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Global Variables

recipe = mongo.db.recipe
user = mongo.db.users


@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/recipe')
def get_recipe():

    return render_template("public/recipe.html", recipes=mongo.db.recipe.find())

@app.route('/create_recipe', methods=["GET", "POST"])
def add_recipe():

    if request.method == "POST":
        req = request.form
        recipe_name = req["recipe_name"]
        course = req["dish_type"]
        prep_time = req["preparation_time"]
        cook_time = req["cooking_time"]
        effort = req["effort"]
        servings = req["servings"]
        description = req["description"]

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
            "recipe_name": recipe_name,
            "recipe_course": course,
            "prep_time": int(prep_time),
            "cooking_time": int(cook_time),
            "effort": effort,
            "servings": int(servings),
            "recipe_description" : description,
            "steps": steps_list,
            "ingredients": ingredient_list
        }

        recipe.insert_one(new_recipe)
        return redirect("/")

    return render_template("public/create_recipe.html")


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
                print(new_user)
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
        

@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserLogin()

    if request.method == "POST":
        if form.validate_on_submit():
            req = request.form
            existing_user = user.find_one({"email": req["email"]})

            if existing_user:
                for fields in existing_user.items():
                    if fields[0] == "password":
                        print("Checking password match")
                        if pbkdf2_sha256.verify(req["password"], fields[1]):
                            print("You can Log In")
                            
                        else:
                            print("Password incorrect")             
            else:
                print("Email not found")

            return render_template("public/login.html", title="Login", form=form)

        else:
            return render_template("public/login.html", title="Login", form=form)   
           
    elif request.method == "GET":
        return render_template("public/login.html", title="Login", form=form)   


@app.errorhandler(404)
def page_not_found(e):
    return render_template("public/404.html"), 404

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)