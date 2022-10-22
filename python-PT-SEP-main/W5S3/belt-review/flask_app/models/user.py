from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
bcrypt = Bcrypt(app)
class User:
  DB = "belt_review"

  def __init__(self,data):
    self.id = data["id"]
    self.first_name = data["first_name"]
    self.last_name = data["last_name"]
    self.email = data["email"]
    self.password = data["password"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

  @classmethod
  def register(cls,user_data):
    data = {
      "first_name":user_data["first_name"],
      "last_name":user_data["last_name"],
      "email":user_data["email"],
      "password":bcrypt.generate_password_hash(user_data["password"])
    }
    query = """
    INSERT INTO users(first_name,last_name,email,password)
    VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);
    """
    result = connectToMySQL(cls.DB).query_db(query,data)
    print("___INSERT USER id___",result)
    return result

  @classmethod
  def get_user_by_email(cls,email):
    data = {"email":email}
    query =  """
    SELECT * FROM users WHERE email = %(email)s;
    """
    result = connectToMySQL(cls.DB).query_db(query,data)
    if len(result) == 0:
      return False
    else:
      return cls(result[0])
  @staticmethod
  def validate_register(user):
    pass
