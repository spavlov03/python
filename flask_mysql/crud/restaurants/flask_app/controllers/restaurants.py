from flask_app import app
from flask import render_template, redirect, request
from flask_app.models import restaurant

@app.route('/')
def index():
    return render_template('index.html')
