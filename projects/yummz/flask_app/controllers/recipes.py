from flask import render_template, redirect ,session,request
from flask_app import app
from flask_app.models import recipe,ingredient

@app.route("/add-recipe",methods=["POST"])
def add_recipe():
  if "user_id" not in session:
        return redirect("/logout")
  data = {
    "recipe_name" : request.form['recipe_name'], 
    "duration": request.form['duration'], 
    "instructions": request.form['instructions'],
    "user_id": session['user_id']
  }
  data2 = {
    "recipe_id" : 
  }
  recipe.Recipe.add_recipe(data,data2)
  return redirect("/dashboard")
