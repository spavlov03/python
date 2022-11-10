from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import user


@app.route("/")
def index(): 
  return render_template('index.html')
@app.route("/login")
def login(): 
  return render_template('login.html')