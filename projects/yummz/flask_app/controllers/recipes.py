from flask import render_template, redirect ,session,request
from flask_app import app
from flask_app.models import recipe,ingredient,user

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
  session['recipe_name'] = request.form['recipe_name']
  recipe.Recipe.add_recipe(data)
  return redirect("/add_ingredients")
@app.route("/add_ingredients")
def add_ingredients():
  data = {"recipe_name": session['recipe_name']}
  curr_recipe = recipe.Recipe.get_recipe_by_name(data)
  session['recipe_id']=curr_recipe[0]['id']
  ingredients = ingredient.Ingredient.get_all_ingredients()
  logged_user = user.User.get_user_by_id({"id":session['user_id']})
  return render_template("add_ingredients.html",logged_user=logged_user,curr_recipe=curr_recipe,ingredients=ingredients)
@app.route("/add_ingredients_to_recipe",methods=["POST"])
def ingredients_add():
  data = {
    "recipe_id": session["recipe_id"]
    ""
  }
