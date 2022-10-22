from flask_app.models import category
from flask_app.config.mysqlconnection import connectToMySQL

class Product:
  DB="sept-products"

  def __init__(self,data):
    self.id = data["id"]
    self.name = data["name"]
    self.price = data["price"]
    self.category = None
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

  @classmethod
  def get_all_products(cls):
    query = "SELECT * FROM products JOIN categories ON products.category_id = categories.id;"
    results = connectToMySQL(cls.DB).query_db(query)
    print("__ALL PRODUCTS___",results)
    products = []
    for row in results:
      product = cls(row)
      # category_date from the join result
      category_data = {
        "id":row["categories.id"],
        "name":row["categories.name"],
        "created_at":row["categories.created_at"],
        "updated_at":row["categories.updated_at"]
      }
      # product_category will be the instance from the Category class
      product_category = category.Category(category_data)
      product.category = product_category
      products.append(product)
    return products

  @classmethod
  def get_category_products(cls,id):
    data = {"id":id}
    query = "SELECT * FROM products LEFT JOIN categories ON products.category_id = categories.id WHERE categories.id = %(id)s;"
    results = connectToMySQL(cls.DB).query_db(query,data)
    print("__ALL PRODUCTS___",results)
    products = []
    for row in results:
      product = cls(row)
      # category_date from the join result
      category_data = {
        "id":row["categories.id"],
        "name":row["categories.name"],
        "created_at":row["categories.created_at"],
        "updated_at":row["categories.updated_at"]
      }
      # product_category will be the instance from the Category class
      product_category = category.Category(category_data)
      product.category = product_category
      products.append(product)
    return products

  @classmethod
  def get_product_by_id(cls,id):
    data = {"id":id}
    query = "SELECT * FROM products LEFT JOIN categories ON categories.id = products.category_id WHERE products.id=%(id)s;"
    results = connectToMySQL(cls.DB).query_db(query,data)
    # LIST OF 1 Item
    print("____GET ONE PRODUCT BY ID____",results)
    product_info = results[0]
    category_data = {
        "id":product_info["categories.id"],
        "name":product_info["categories.name"],
        "created_at":product_info["categories.created_at"],
        "updated_at":product_info["categories.updated_at"]
      }
      # product_category will be the instance from the Category class
    product_category = category.Category(category_data)
    product = cls(product_info)
    product.category = product_category 
    return product
  @classmethod
  def create_product(cls,form_data):
    query = "INSERT INTO products (name,price,category_id) VALUES (%(name)s,%(price)s,%(category_id)s);"
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

  @classmethod
  def update_product(cls,data):
    query = "UPDATE products SET name=%(name)s,price=%(price)s, category=%(category)s WHERE id=%(id)s;"
    result = connectToMySQL(cls.DB).query_db(query,data)
    # result is None!
    print("__ UPDATE PRODUCT___",result)
    return result