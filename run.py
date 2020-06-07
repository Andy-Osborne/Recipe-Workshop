import os
from flask import Flask, render_template, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("public/index.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug=True)