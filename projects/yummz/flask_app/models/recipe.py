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
  def add_recipe(cls,data): 
    query = "INSERT INTO recipes (recipe_name,duration,instructions,user_id) VALUES (%(recipe_name)s,%(duration)s,%(instructions)s,%(user_id)s);"
    result = connectToMySQL(cls.DB).query_db(query,data)
    return result 

  @classmethod
  def get_recipe_by_name(cls,data):
    query = "SELECT * FROM recipes WHERE recipe_name=%(recipe_name)s"
    result = connectToMySQL(cls.DB).query_db(query,data)
    return result
