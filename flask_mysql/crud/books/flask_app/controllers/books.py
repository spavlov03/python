from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import book

@app.route("/books")
def all_books():
    books = book.Book.get_all_books()
    return render_template("books.html", books=books)
@app.route("/new-book",methods=["POST"])
def add_book():
    print("BOOK DATA IS----",request.form)
    book.Book.new_book(request.form)
    return redirect("/books")
