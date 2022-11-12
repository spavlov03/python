from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user




@app.route("/")
def index():
  return render_template('index.html')


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/signup")
def signup():
  return render_template('signup.html')


@app.route("/register",methods=["POST"])
def register():
  if not user.User.validate_user(request.form):
        return redirect("/")
  data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            "password":bcrypt.generate_password_hash(request.form['password'])
        }
  user_id = user.User.register(data)
  session['user_id'] = user_id

  return redirect("/login")



