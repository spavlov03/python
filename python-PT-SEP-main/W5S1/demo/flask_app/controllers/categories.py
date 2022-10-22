from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import category


@app.route("/")
def index():
  #file.class.class_method()
  return render_template("index.html")

@app.route("/add-category",methods=["POST"])
def add_category():
  #file.class.class_method()
  category.Category.create_category(request.form)
  return redirect("/")