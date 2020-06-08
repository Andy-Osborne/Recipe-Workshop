import os
from flask import Flask, render_template, url_for, redirect, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("NONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/recipe')
def get_recipe():

    return render_template("public/recipe.html", recipes=mongo.db.recipe.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)