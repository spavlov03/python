from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user,recipe,ingredient
import requests
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/login-user",methods=["POST"])
def login_user(): 
  users = user.User.get_user_by_email(request.form)
  if not users:
      flash("Invalid Email/Password","login")
      return redirect('/login')
  if not bcrypt.check_password_hash(users.password, request.form['password']):
      flash("Invalid Email/Password","login")
      return redirect('/login')
  session['user_id'] = users.id
  return redirect("/dashboard")


@app.route("/signup")
def signup():
  return render_template('signup.html')


@app.route("/register",methods=["POST"])
def register():
  if not user.User.validate_user(request.form):
        return redirect("/signup")
  data = {
            "first_name":request.form['first_name'],
            "last_name":request.form['last_name'],
            "email":request.form['email'],
            "password":bcrypt.generate_password_hash(request.form['password'])
        }
  user_id = user.User.register(data)
  session['user_id'] = user_id

  return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
  data = {"id":session['user_id']}
  logged_user = user.User.get_user_by_id(data)
  recipes = recipe.Recipe.get_all_recipes()
  return render_template('dashboard.html',logged_user=logged_user, recipes=recipes)


@app.route("/logout")
def logout():
  session.clear()
  return redirect('/')





