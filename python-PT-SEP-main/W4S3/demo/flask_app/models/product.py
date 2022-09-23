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
  
  @classmethod
  def get_product_by_id(cls,id):
    data = {"id":id}
    query = "SELECT * FROM products WHERE id=%(id)s;"
    results = connectToMySQL(cls.DB).query_db(query,data)
    # LIST OF 1 Item
    print("____GET ONE PRODUCT BY ID____",results)
    return cls(results[0])
  @classmethod
  def create_product(cls,form_data):
    query = "INSERT INTO products (name,price,category) VALUES (%(name)s,%(price)s,%(category)s);"
    result = connectToMySQL(cls.DB).query_db(query,form_data)
    # result is the id for the product
    print("__ CREATE PRODUCT___",result)
    return result

  @classmethod
  def delete_product(cls,id):
    data = {"id":id}
    query = "DELETE FROM products WHERE id=%(id)s;"
    result = connectToMySQL(cls.DB).query_db(query,data)
    # result is None!
    print("__ DELETE PRODUCT___",result)
    return result