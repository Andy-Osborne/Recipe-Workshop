from flask import render_template

from app import app


# 404 Page

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# 410 Page

@app.errorhandler(410)
def page_gone(e):
    return render_template("410.html"), 410


# 500 Page

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500
