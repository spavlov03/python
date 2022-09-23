from flask_app.config.mysqlconnection import connectToMySQL

class Product:
  DB="sept-products"

  def __init__(self,data):
    self.id = data["id"]
    self.name = data["name"]
    self.price = data["price"]
    self.category = data["category"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

  @classmethod
  def get_all_products(cls):
    query = "SELECT * FROM products;"
    results = connectToMySQL(cls.DB).query_db(query)
    print("__ALL PRODUCTS___",results)
    products = []
    for row in results:
      products.append(cls(row))
    return products