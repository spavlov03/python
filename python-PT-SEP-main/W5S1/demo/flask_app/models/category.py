from flask_app.config.mysqlconnection import connectToMySQL

class Category:
  DB="sept-products"

  def __init__(self,data):
    self.id = data["id"]
    self.name = data["name"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

  @classmethod
  def get_all_categories(cls):
    query = "SELECT * FROM categories;"
    results = connectToMySQL(cls.DB).query_db(query)
    print("__ALL Categories ___",results)
    categories = []
    for row in results:
      categories.append(cls(row))
    return categories

  @classmethod
  def create_category(cls,form_data):
    query = "INSERT INTO categories (name) VALUES (%(name)s);"
    result = connectToMySQL(cls.DB).query_db(query,form_data)
    # result is the id for the product
    print("__ CREATE Category ___",result)
    return result