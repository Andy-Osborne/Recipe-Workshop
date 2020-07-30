import os
from app import app
from flask_pymongo import PyMongo
import cloudinary as cloudinary
import cloudinary.uploader
import cloudinary.api

if os.path.exists("env.py"):
    import env

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
