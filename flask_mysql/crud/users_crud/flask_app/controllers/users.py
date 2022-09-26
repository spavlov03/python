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
@app.route("/users/<id>/delete")
def delete_user(id):
    user.User.delete_user(id)
    return redirect("/")
@app.route("/users/<id>/show")
def show_user(id):
    one_user = user.User.get_user_by_id(id)
    return render_template("show_user.html", one_user = one_user)
@app.route('/users/<id>/edit')
def edit_one_user(id):
    one_user = user.User.get_user_by_id(id)
    return render_template("edit_user.html", one_user = one_user)
@app.route("/users/<id>/edit-user", methods=['POST'])
def edit_user(id):
    print("EDITING.....",request.form)
    user.User.edit_user(request.form)
    return redirect("/")
