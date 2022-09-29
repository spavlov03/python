from re import T
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    DB = "users_db"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("First Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last Name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ALL USERS___", results)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    @classmethod
    def get_user_by_id(cls,id):
        data = {"id":id}
        query = "SELECT * FROM users WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("__SHOWING USER__",result)
        return result


    @classmethod
    def add_user(cls, form_data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL(cls.DB).query_db(query, form_data)
        print("___ Add User ___", result)
        return result

    @classmethod
    def delete_user(cls,id):
        data = {"id":id}
        query = "DELETE FROM users WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("___ DELETE USER___",result)
        return result

    @classmethod
    def edit_user(cls, data):
        print("DATA IS ----",data)
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("___ UPDATE USER___",result)
        return result

