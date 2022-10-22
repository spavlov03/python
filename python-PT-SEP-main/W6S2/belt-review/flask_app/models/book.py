from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models import user
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
    self.creator = None
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
    query = """
    SELECT * FROM books JOIN users on books.user_id = users.id ORDER BY books.created_at;
    """
    results = connectToMySQL(cls.DB).query_db(query)
    books = []
    for row in results:
      book = cls(row)
      book_creator_info = {
        "id":row["users.id"],
        "first_name":row["first_name"],
        "last_name":row["last_name"],
        "email":row["email"],
        "password":row["password"],
        "created_at":row["created_at"],
        "updated_at":row["updated_at"]
      }
      creator = user.User(book_creator_info)
      book.creator = creator
      books.append(book)
    return books

  @classmethod
  def get_book(cls,book_id):
    data = {"id":book_id}
    query = """
    SELECT * FROM books JOIN users on books.user_id = users.id WHERE books.id = %(id)s;
    """
    results = connectToMySQL(cls.DB).query_db(query,data)
    book = cls(results[0])
    return book

  @classmethod
  def update_book(cls,data):
    query = """
    UPDATE books SET 
    title = %(title)s, author = %(author)s, publisher = %(publisher)s, publish_date = %(publish_date)s, user_id = %(user_id)s 
    WHERE books.id = %(id)s;
    """
    return connectToMySQL(cls.DB).query_db(query,data)

  @classmethod
  def get_user_books(cls,user_id):
    data={"user_id":user_id}
    query = """
    SELECT * FROM books WHERE books.user_id = %(user_id)s;
    """
    results = connectToMySQL(cls.DB).query_db(query,data)
    books = []
    for row in results:
      book = cls(row)
      books.append(book)
    return books

  @classmethod
  def delete_book(cls,book_id):
    data = {"id":book_id}
    query = """
    DELETE FROM books WHERE id=%(id)s;
    """
    return connectToMySQL(cls.DB).query_db(query,data)