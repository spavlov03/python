from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import recipe,user
from flask import flash

class Recipe:
    DB = "recipes"

    def __init__(self,data): 
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.under_30_min = data['under_30_min']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def add_recipe(cls,data):
        query = "INSERT INTO recipes (name,description,instructions,date_made,under_30_min,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(date_made)s,%(under_30_min)s,%(user_id)s);"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("___ADDING NEW RECIPE",result)
        return result
    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe_creator_info = {
                "id":row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            creator = user.User(recipe_creator_info)
            recipe.creator = creator
            recipes.append(recipe)
        return recipes
    @classmethod
    def get_one_recipe_by_id(cls,data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe_creator_info = {
                "id":row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            creator = user.User(recipe_creator_info)
            recipe.creator = creator
            recipes.append(recipe)
        return recipes[0]

    @classmethod
    def get_recipe_by_id(cls,id):
        data = {"id":id}
        query = "SELECT * FROM recipes WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("__SHOWING RECIPE__",result)
        return result[0]
    @classmethod
    def edit_recipe(cls,data):
        print("EDIT DATA IS ----",data)
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,date_made=%(date_made)s,under_30_min=%(under_30_min)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("EDDITED RECIPE IS ----",result)
        return result
    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("DELETED RECIPE----",result)
        return result
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.","recipe")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.","recipe")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters.","recipe")
            is_valid = False
        return is_valid