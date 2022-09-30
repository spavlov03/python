from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    DB = "books_schema"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.fav_books = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL(cls.DB).query_db(query)
        print("___GETTING ALL AUTHORS___",results)
        authors = []
        for row in results:
            authors.append(cls(row))
        return authors 
    @classmethod
    def new_author(cls,author_data): 
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        results = connectToMySQL(cls.DB).query_db(query,author_data)
        print("___ADDING NEW AUTHOR___",results)
        return results
    @classmethod
    def get_author_with_books(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE authors.id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("AUTHORS")
        author = cls(result[0])
        for row in result: 
            book_data = {
                "id": row["books.id"],
                "title": row["title"],
                "num_of_pages":row["num_of_pages"],
                "created_at":row["books.created_at"], 
                "updated_at":row["books.updated_at"]
            }
            author.fav_books.append(book.Book(book_data))
        return author