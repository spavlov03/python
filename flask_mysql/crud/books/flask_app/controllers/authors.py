from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import author

@app.route("/")
def index():
    return redirect("/authors")
@app.route("/authors")
def all_authors():
    authors = author.Author.get_all_authors()
    return render_template("authors.html", authors=authors)
@app.route("/new-author",methods=["POST"])
def add_author():
    print("AUTHOR DATA IS----",request.form)
    author.Author.new_author(request.form)
    return redirect("/authors")
    