from flask_app.config.mysqlconnection import connectToMySQL

class Ingredient: 
  DB = "yummz"

  def __init__(self,data):
    self.id = data['id']
    self.name = data['name']
    self.type = data['type']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']

  @classmethod
  def get_all_ingredients(cls):
    query = "SELECT * FROM ingredients"
    result = connectToMySQL(cls.DB).query_db(query)
    return result