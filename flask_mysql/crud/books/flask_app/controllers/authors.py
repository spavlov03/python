from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import author,book

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
@app.route("/authors/<int:id>")
def show_author(id):
    data = {"id":id}
    one_author = author.Author.get_author_by_id(id) 
    books = book.Book.get_all_books()
    authors_books = author.Author.get_author_with_books(data)
    print("authors books are-----",authors_books)
    return render_template("author.html",one_author=one_author, books=books,authors_books = authors_books)
@app.route("/authors/<int:id>/add-fav",methods=["POST"])
def add_author_fav(id):
    data = {
        "book_id": request.form['book_id'], 
        "author_id": id
    }
    author.Author.add_author_fav_book(data)
    return redirect(f"/books/{request.form['book_id']}")