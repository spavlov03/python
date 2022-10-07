from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import ride

@app.route("/rides/new")
def new_ride():
    if "user_id" not in session:
        return redirect("/logout")
    return render_template("request_ride.html")