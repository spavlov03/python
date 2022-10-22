from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models import user,book

@app.route("/dashboard")
def dashboard():
  if "user_id" not in session:
    return redirect("/")
  logged_in_user = user.User.get_user_by_id(session["user_id"])
  books = book.Book.get_all_books()
  return render_template("dashboard.html",logged_in_user=logged_in_user,books=books)


@app.route("/new/book")
def add_book():
  if "user_id" not in session:
    return redirect("/")
  logged_in_user = user.User.get_user_by_id(session["user_id"])
  return render_template("add-book.html",logged_in_user=logged_in_user)

@app.route("/add-book",methods=["POST"])
def create_book():
  if "user_id" not in session:
    return redirect("/")
  if book.Book.validate_book(request.form):
    book.Book.create_book(request.form)
    # IF YOU DONT PASS THE USER_ID IN THE FORM YOU NEED TO PASS IT TO THE MODEL FROM THE SESSION
    # book.Book.create_book(request.form,session["user_id"])
    return redirect("/dashboard")
  return redirect("/new/book")