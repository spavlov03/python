from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app

class Book:
  DB = "belt_review"

  def __init__(self,data):
    self.id = data["id"]
    self.title = data["title"]
    self.author = data["author"]
    self.publisher = data["publisher"]
    self.publish_date = data["publish_date"]
    self.user_id = data["user_id"]
    self.created_at = data["created_at"]
    self.updated_at = data["updated_at"]

  @staticmethod
  def validate_book(book):
    is_valid = True
    if len(book["title"]) < 4:
      flash("title must be at least 4 characters")
      is_valid = False
    if len(book["author"]) < 5:
      flash("author must be at least 5 characters")
      is_valid = False
    if len(book["publisher"]) > 20 or len(book["publisher"]) <= 2:
      flash("publisher must be at least 20 characters")
      is_valid = False
    if not book["publish_date"]:
      flash("Date published must be added")
      is_valid = False
    return is_valid


  @classmethod
  def create_book(cls,data):
    query = """
    INSERT INTO books (title,author,publisher,publish_date,user_id)
    VALUES (%(title)s,%(author)s,%(publisher)s,%(publish_date)s,%(user_id)s);
    """
    return connectToMySQL(cls.DB).query_db(query,data)

  @classmethod
  def get_all_books(cls):
    pass