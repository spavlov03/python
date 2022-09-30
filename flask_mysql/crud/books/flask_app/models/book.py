from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author
class Book:
    DB = "books_schema"

    def __init__(self,data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors = []

    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books"
        results = connectToMySQL(cls.DB).query_db(query)
        print("___GETTING ALL BOOKS___",results)
        books = []
        for row in results:
            books.append(cls(row))
        return books
    @classmethod
    def new_book(cls,book_data): 
        query = "INSERT INTO books (title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s)"
        results = connectToMySQL(cls.DB).query_db(query,book_data)
        print("___ADDING NEW BOOK___",results)
        return results
    @classmethod
    def get_books_with_author(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE books.id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("BOOKS")
        book = cls(result[0])
        for row in result: 
            author_data = {
                "id": row["authors.id"],
                "name": row["name"],
                "created_at":row["authors.created_at"], 
                "updated_at":row["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))
        return book
    