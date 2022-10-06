from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import user,message

@app.route("/wall")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session['user_id']}
    return render_template('wall.html',user = user.User.get_user_by_id(data))

    

