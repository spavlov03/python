from flask import render_template, redirect, request,session
from flask_app import app
from flask_app.models import user


@app.route("/")
def index():
    if "user_id" in session:
        return redirect("/wall")
    return render_template('index.html')
@app.route("/register",methods=["POST"])
def register(): 
    if not user.User.validate_register(request.form):
        return redirect("/")
    user_id = user.User.register(request.form)
    session['user_id'] = user_id
    return redirect("/wall")

@app.route('/login',methods=["POST"])
def login():
    logged_in_user = user.User.validate_login(request.form)
    if not logged_in_user:
        return redirect('/')
    session['user_id'] = logged_in_user.id
    return redirect("/wall")
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
