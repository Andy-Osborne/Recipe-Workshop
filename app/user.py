from flask import (render_template, url_for, redirect, request, flash,
                   session, jsonify)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from passlib.hash import pbkdf2_sha256 as p256
from bson.objectid import ObjectId

from app import app
from app.config import user, recipe
from app.helpers import (upload_image, no_change_check, new_pass_check,
                         email_update, password_update)


class UserRegistration(FlaskForm):
    username = StringField("Username",
                           validators=[DataRequired(), Length(min=3, max=20),
                                       Regexp('^[a-zA-Z0-9]*$',
                                              message="Please use only \
                                                   lowercase, uppercase or \
                                                        numbers")])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     Length(min=8)])
    confirm_password = PasswordField("Confirm Password",
                                     validators=[DataRequired(),
                                                 EqualTo("password")])
    submit = SubmitField("Sign Up")


class UserLogin(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


# Registration

@app.route("/register", methods=["GET", "POST"])
def user_registration():

    username = session["username"] if "username" in session else ""

    if username != "":
        return redirect(url_for("profile", username=username))

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
            session["username"] = req["username"]
            return redirect(url_for("profile",
                                    username=session["username"]))

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


# Login

@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserLogin()

    username = session["username"] if "username" in session else ""

    if username != "":
        return redirect(url_for("profile", username=username))

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
                                url_for("profile", username=session["username"]
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


# Logout

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# User Profile Page

@app.route("/profile/<username>")
def profile(username):
    user_profile_check = user.find_one({"username": username})

    # Assigns a value tt the variable based on whether the user exists or not
    user_profile = user_profile_check if user_profile_check is not None else ""
    recipe_count = recipe.count_documents({"recipe_author": username})

    return render_template("profile.html", username=user_profile,
                           recipes=recipe.find(), recipe_count=recipe_count,
                           page="profile")


# Update User Profile

@app.route("/profile/update/<username>", methods=["POST", "GET"])
def update_profile(username):

    user_profile = user.find_one({"username": username})

    # Prevents user who is not profile owner from updating it

    username = session["username"] if "username" in session else ""

    if username != user_profile["username"]:
        return redirect("/")

    if request.method == "POST":
        reqf = request.form

        profile_image = request.files["profile-image"]

        # The below uses the Cloudinary Upload Code helper Function
        image_url, image_id = upload_image(profile_image, "profile")

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


# Update User Account Information

@app.route("/profile/account_management", methods=["POST"])
def update_account():
    req = request.form

    user_id = req["user_id"]
    new_email = req["email"]
    password = req["password"]
    new_pass = ""
    conf_pass = ""

    # Checks to see if a new password has been submitted

    if "new-password" in req:
        new_pass = req["new-password"]
        conf_pass = req["conf-password"]

    user_profile = user.find_one({"_id": ObjectId(user_id)})
    current_pass = user_profile["password"]
    current_email = user_profile["email"]

    # Check to see if no new pasword and email has not changed

    if no_change_check(current_email, new_email, current_pass, new_pass):
        return jsonify(
            {"error": "Account not updated - no new information given."})

    # Verifies the password entered matches the one registered

    if p256.verify(password, current_pass):

        # Checks to see if a new email and pass has been entered

        if current_email != new_email and new_pass != "":

            # If new pass and email, checks to see if they match

            if new_pass_check(new_pass, conf_pass):

                # If new pass match then it updates email and pass
                email_update(user_id, new_email)
                password_update(user_id, new_pass)
                return jsonify(
                    {"success": "Account successfully updated!"})
            else:
                return jsonify(
                    {"error": "New passwords do not match."})

        # If no new password is entered, it runs the update email function

        elif current_email != new_email:

            email_update(user_id, new_email)
            return jsonify({"success": "Email successfully updated!"})

        # If no new email entered, checks to see if new password was entered

        elif new_pass_check(new_pass, conf_pass):

            # If new pass match then it updates pass
            password_update(user_id, new_pass)
            return jsonify(
                {"success": "Password successfully updated!"})

        else:
            return jsonify(
                {"error": "New passwords do not match."})

    # If account password does not match. Below is shown to user.

    else:
        return jsonify({"error": "Incorrect current password entered."})


# Below code taken from a rip tutorial and edited to only show the DD/MM/YYYY

@app.template_filter("formatdatetime")
def format_datetime(value, format="%d %b %Y"):
    if value is None:
        return ""
    return value.strftime(format)
