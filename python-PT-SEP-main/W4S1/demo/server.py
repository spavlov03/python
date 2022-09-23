from flask import Flask,render_template,redirect,request,session

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/")
def index():
  return render_template("index.html")

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
if __name__ == "__main__":
  app.run(debug=True,port=8000)
