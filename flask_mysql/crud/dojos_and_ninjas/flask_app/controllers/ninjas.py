from flask_app import app
from flask import render_template, redirect, request,session
from flask_app.models import ninja, dojo

@app.route("/ninjas")
def ninja_index():
    return render_template("ninjas.html",dojos=dojo.Dojo.get_all_dojos())


@app.route("/create/ninja",methods=["POST"])
def add_ninja():
    #print("DATA IS .........",request.form)
    ninja.Ninja.new_ninja(request.form)
    return redirect("/")

@app.route("/ninjas/delete/<id>")
def delete_ninja(id):
    ninja.Ninja.delete_ninja(id)
    dojo_id = int(session['dojo-id'])
    return redirect(f"/dojo/{dojo_id}")

@app.route("/ninjas/edit/<id>")
def edit_ninja(id):
    one_ninja = ninja.Ninja.get_ninja_by_id(id)
    #print("ONE NINJA IS----",one_ninja)
    return render_template("edit-ninja.html", one_ninja=one_ninja)
@app.route("/ninja/edit/<id>",methods=["POST"])
def ninja_edit(id):
    ninja.Ninja.edit_ninja(request.form)
    dojo_id = int(session['dojo-id'])
    return redirect(f"/dojo/{dojo_id}")

