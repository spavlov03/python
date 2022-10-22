from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import product,category

@app.route("/")
def index():
  #file.class.class_method()
  products = product.Product.get_all_products()
  return render_template("index.html",products=products)

@app.route('/create-product')
def create_product():
  categories = category.Category.get_all_categories()
  return render_template("product-form.html",categories=categories)

@app.route("/add-product",methods=["POST"])
def add_product():
    print("Hello",request.form)
    product.Product.create_product(request.form)
    return redirect("/")

@app.route("/products/<id>")
def get_product(id):
  #file.class.class_method()
  one_product = product.Product.get_product_by_id(id) 
  return render_template("product-details.html",product=one_product)

@app.route("/products/<id>/delete")
def delete_product(id):
  #file.class.class_method()
  product.Product.delete_product(id)
  return redirect('/')

@app.route("/products/<id>/edit")
def edit_product(id):
  # GET PRODUCT BY ID TO fill the form
  the_product = product.Product.get_product_by_id(id)
  categories = category.Category.get_all_categories()
  return render_template("edit-product.html",product=the_product,categories=categories)

@app.route("/products/<id>/update",methods=["POST"])
def update_product(id):
  product.Product.update_product(request.form)
  return redirect(f"/products/{id}")
