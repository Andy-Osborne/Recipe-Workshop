from flask import (render_template, request, session, jsonify)
from bson.objectid import ObjectId


from app import app
from app.config import recipe, newsletter

# Landing Page


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


# Newsletter Sign Up Logic

@app.route("/newsletter",  methods=["POST"])
def newsletter_register():

    email = request.form["email"]
    duplicate_search = newsletter.find_one({"email": email})

    # Checks to see if a username is in session then assigns to variable

    username = session["username"] if "username" in session else ""

    # Checks to see if email is already in newsletter collection

    if not duplicate_search:

        # Checks to see if username variable is empty and only inserts email

        if username == "":
            new_signup = {
                "email": email
            }

            newsletter.insert_one(new_signup)
            return jsonify(
                {"success": "Thank you! You've joined our newsletter list."})

        # If there is info in username variable, inserts email and username

        else:
            new_signup = {
                "email": email,
                "username": username
            }

            newsletter.insert_one(new_signup)
            return jsonify(
                {"success": "Thank you! You've joined our newsletter list."})

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
                {"error": "Looks like you're already in our newsletter list!"})

        else:

            # If no given username & email is already in newsletter collection

            return jsonify(
                {"error": "Looks like you're already in our newsletter list!"})
