from passlib.hash import pbkdf2_sha256 as p256
from bson.objectid import ObjectId

from app.config import user, cloud


# Recipe Helper Functions

# Takes the ingredients from the recipe form and assigns to a list

def recipe_ingredients(req):
    ingredient_list = []

    for key in req.keys():
        if key == "ingredients":
            for value in req.getlist(key):
                ingredient_list.append(value)

    return ingredient_list


# Takes the steps from the recipe form and assigns to to a list

def recipe_steps(req):
    steps_list = []

    for key in req.keys():
        if key == "step":
            for value in req.getlist(key):
                steps_list.append(value)

    return steps_list


# Account Update Helper Functions

def no_change_check(email, new_email, password, new_pass):
    # checks if new password has not been entered
    old_pass = True if new_pass == "" else False
    # checks if new password entered matches existing password
    pass_verify = (True if not old_pass
                   and p256.verify(new_pass, password)
                   else False)
    # checks if the email has not changed
    same_email = True if email == new_email else False

    # checks if it's the same email and no new pass
    if same_email and old_pass or same_email and pass_verify:
        return True
    else:
        return False


def new_pass_check(new, conf):
    # checks if new and conf passwords match
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


# Universal Helper

# Cloudinary Upload Code

"""
This takes in the variable which has been assigned the request file,
it then uploads the image - resizes and compresses image.
The folder_string variable is the name of the folder to be used in
Cloudinary's website.
"""


def upload_image(vairable, folder_string):
    uploaded_image = cloud.upload(vairable, width=500, height=500,
                                  quality="auto",
                                  folder=f"Recipe_Workshop/{folder_string}/")

    image_url = uploaded_image.get("secure_url")
    image_id = uploaded_image.get("public_id")
    return image_url, image_id
