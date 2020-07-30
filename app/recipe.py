from flask import (render_template, url_for, redirect, request,
                   session, jsonify)
from bson.objectid import ObjectId
from datetime import datetime

from app import app
from app.config import cloud, recipe
from app.helpers import recipe_ingredients, recipe_steps, upload_image


# Recipe Page

@app.route("/recipe/<recipe_id>/<recipe_name>")
def get_recipe(recipe_id, recipe_name):
    recipe_view = recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe_view)


# Add Recipe Page

@app.route("/create_recipe", methods=["GET", "POST"])
def add_recipe():

    username = session["username"] if "username" in session else ""

    if username == "":
        return redirect("/login")

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

        ingredient_list = recipe_ingredients(req)
        steps_list = recipe_steps(req)

        # Below is cloudinary helper function to upload recipe image

        image_url, image_id = upload_image(image, "recipe")

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


# Manage Recipe

@app.route("/manage/<recipe_id>")
def manage_recipe(recipe_id):

    edit_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})

    # Prevents user who is not recipe owner from editing recipe

    username = session["username"] if "username" in session else ""

    if username != edit_recipe["recipe_author"]:
        return redirect("/")

    return render_template("manage_recipe.html", recipe=edit_recipe)


# Updating Recipe

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

        ingredient_list = recipe_ingredients(req)
        steps_list = recipe_steps(req)

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

            image_url, image_id = upload_image(image, "recipe")

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

    username = session["username"] if "username" in session else ""

    if username != recipe_check["recipe_author"]:
        return redirect("/")

    else:
        recipe.delete_one({"_id": ObjectId(recipe_id)})

        # The below deletes the recipe image from cloudinary

        public_id = recipe_check["image_id"]
        cloud.destroy(public_id)

    return redirect(url_for("profile", username=session["username"]))


# Handles the logic of a user liking or removing their like from a recipe

@app.route("/like/<recipe_id>", methods=["POST"])
def like(recipe_id):
    find_recipe = recipe.find_one({"_id": ObjectId(recipe_id)})

    """
    The below checks if username is in the recipe liked_by field. If it is
    it decrements the likes of recipe by 1 and removes username from field.
    If the username is not, it increases likes by 1 and adds username to field.
    """

    if session["username"] not in find_recipe["liked_by"]:
        recipe.update_one(
            {"_id": ObjectId(recipe_id)},
            {
                "$inc": {"likes": 1},
                "$push": {"liked_by": session["username"]}
            })
        new_like = recipe.find_one({"_id": ObjectId(recipe_id)})["likes"]
        return jsonify({"add": new_like})
    else:
        recipe.update_one(
            {"_id": ObjectId(recipe_id)},
            {
                "$inc": {"likes": -1},
                "$pull": {"liked_by": session["username"]}
            })
        new_like = recipe.find_one({"_id": ObjectId(recipe_id)})["likes"]
        return jsonify({"remove": new_like})
