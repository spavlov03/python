from flask import render_template, redirect, request,session,flash
from flask_app import app
from flask_app.models import recipe,user

@app.route("/recipes")
def dashboard():
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session['user_id']}
    all_recipes = recipe.Recipe.get_all_recipes()
    one_user = user.User.get_user_by_id(data)
    session['first_name'] = one_user.first_name
    #print("SESSION FIRST NAME------",session['first_name'])
    return render_template('recipes.html',user = one_user,all_recipes=all_recipes)

@app.route("/recipes/new")
def new_recipe():
    if "user_id" not in session:
        return redirect("/logout")
    data = {"id": session['user_id']}
    return render_template('new_recipe.html',user = user.User.get_user_by_id(data))
@app.route("/add_recipe",methods=['POST'])
def add_recipe():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "date_made": request.form['date_made'],
        "under_30_min": request.form['under_30_min'],
        "user_id": session['user_id']
    }
    recipe.Recipe.add_recipe(data)
    return redirect('/recipes')
@app.route("/recipes/<int:id>")
def show_recipe(id):
    if "user_id" not in session:
        return redirect("/logout")
    one_recipe = recipe.Recipe.get_recipe_by_id(id)
    return render_template("show_recipe.html",one_recipe = one_recipe,user_first_name=session['first_name'])