from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import dojo

@app.route("/")
def index():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("dojos.html", dojos=dojos)