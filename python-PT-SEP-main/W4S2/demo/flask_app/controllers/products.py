from flask_app import app
from flask import render_template,redirect,session,request
from flask_app.models import product
@app.route("/")
def index():
  #file.class.class_method()
  products = product.Product.get_all_products()
  return render_template("index.html",products=products)

@app.route("/add-product",methods=["POST"])
def add_product():
    print("Hello",request.form)
    print("+++++NAME+++++",request.form["name"])
    if "products" in session:
      # append to the session
      # WE CANT APPEND DIRECTLY TO THE SESSION VALUES
      products = session["products"]
      products.append(request.form)
      session["products"] = products
    else:
      # first time only add an list of that product
      session["products"] = [request.form]
      # WHAT IF WE ONLY WANT THE NAME IN SESSION
      #session["name"] = request.form["name"]
    return redirect("/")

@app.route('/clear-session')
def clear():
  session.clear()
  # session.pop("products")
  return redirect('/')