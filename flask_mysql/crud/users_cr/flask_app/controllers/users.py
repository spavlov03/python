from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import user


@app.route("/")
def index():
    # file.class.class_method()
    users = user.User.get_all_users()
    return render_template("all_users.html", users=users)

@app.route("/new-user")
def new_user():
    # file.class.class_method()
    return render_template("add_user.html")

@app.route("/add-user", methods=["POST"])
def add_user():
    print("Hello", request.form)
    user.User.add_user(request.form)
    return redirect("/")
