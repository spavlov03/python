from flask import render_template, redirect, request,session
from flask_app import app
from flask_app.models import dojo,ninja

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojo_index():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("dojos.html", dojos=dojos)

@app.route("/create/dojo",methods=["POST"])
def add_dojo():
    print("DATA IS .........",request.form)
    dojo.Dojo.new_dojo(request.form)
    return redirect("/dojos")

@app.route("/dojo/<int:id>")
def show_dojos(id):
    data = {
        "id": id,
    }
    session['dojo-id'] = id
    return render_template("dojo-show.html",dojo = dojo.Dojo.get_one_with_ninjas(data))

