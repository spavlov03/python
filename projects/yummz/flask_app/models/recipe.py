from flask_app.config.mysqlconnection import connectToMySQL

class Recipe: 
  DB = "yummz"

  def __init__(self,data):
    self.id = data['id']
    self.recipe_name = data['recipe_name']
    self.duration = data['duration']
    self.instructions = data['instructions']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    self.user_id = data['user_id']

  @classmethod
  def get_all_recipes(cls):
    query = "SELECT * FROM recipes"
    result = connectToMySQL(cls.DB).query_db(query)
    return result

  @classmethod
  def add_recipe(cls,data,data2): 
    query = "INSERT INTO recipes (recipe_name,duration,instructions,user_id) VALUES (%(recipe_name)s,%(duration)s,%(instructions)s,%(user_id)s);"
    result = connectToMySQL(cls.DB).query_db(query,data)
    query2 = "INSERT INTO recipes_has_ingredients (recipe_id,ingredient_id,ingredient_qty) VALUES (%(recipe_id)s,%(ingredient_id)s,%(ingredient_qty)s)"
    result2 = connectToMySQL(cls.DB).query_db(query,data2)
    return result and result2