from flask import render_template

from app import app


# Privacy Page

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# Advertise With Us Page

@app.route("/advertise")
def advertise():
    return render_template("advertise.html")
