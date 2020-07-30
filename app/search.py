from flask import render_template, url_for, redirect, request
from flask_paginate import Pagination, get_page_parameter

from app import app
from app.config import recipe

# Search Form


@app.route("/search", methods=["POST"])
def get_search():
    return redirect(url_for("search_recipes",
                            search_term=request.form.get("search_field")))

# Search Results Page


@app.route("/search/<search_term>")
def search_recipes(search_term):

    # The below creates the index for the text search and defines the fields.

    recipe.create_index([
        ("recipe_name", "text"),
        ("ingredients", "text"),
        ("recipe_course", "text"),
        ("recipe_description", "text"),
        ("recipe_author", "text")
    ])

    # Below is used for flask-paginate

    search = False
    q = request.args.get("q")
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)

    # Restricts the amount of results per page

    per_page = 4

    """
    This uses the mongodb text search functionality, sorts the results by it's
    metascore, skips a X results based on page variable less 1, and
    limits the returned in results on each page based on the variable per_page
    """

    search_result = recipe.find({"$text": {"$search": search_term}},
                                {"score": {"$meta": "textScore"}}).sort([
                                    ("score", {"$meta": "textScore"})]).skip(
                                        (page - 1) * per_page).limit(per_page)

    # Records the amount of items that match the search criteria

    search_count = recipe.count_documents({"$text": {"$search": search_term}})

    pagination = Pagination(page=page, per_page=per_page, total=search_count,
                            search=search, record_name="search_result",
                            css_framework="bootstrap4")

    return render_template("search.html", search_term=search_term,
                           search_result=search_result, count=search_count,
                           pagination=pagination)
