from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import category,product



@app.route("/add-category",methods=["POST"])
def add_category():
  #file.class.class_method()
  category.Category.create_category(request.form)
  return redirect("/")

@app.route("/categories/<id>")
def get_category_products(id):
  #file.class.class_method()
  products = product.Product.get_category_products(id)
  return render_template("/category-products.html",products=products)