from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import book,author

@app.route("/books")
def all_books():
    books = book.Book.get_all_books()
    return render_template("books.html", books=books)
@app.route("/new-book",methods=["POST"])
def add_book():
    print("BOOK DATA IS----",request.form)
    book.Book.new_book(request.form)
    return redirect("/books")
@app.route("/books/<int:id>")
def show_book(id):
    data = {"id":id}
    one_book = book.Book.get_book_by_id(id) 
    authors = author.Author.get_all_authors()
    books_authors = book.Book.get_books_with_author(data)
    print("book authors are-----",books_authors)
    return render_template("book.html",one_book=one_book, authors=authors,books_authors=books_authors)
@app.route("/books/<int:id>/add-fav",methods=["POST"])
def add_book_fav(id):
    data = {
        "author_id": request.form['author_id'], 
        "book_id": id
    }
    book.Book.add_book_fav_author(data)
    return redirect(f"/books/{id}")