from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r"^.{8,}$")


class User:
    DB = "yummz"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls, user_data):
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL(cls.DB).query_db(query, user_data)
        #print("___ADDING NEW USER___",result)
        return result
    
    @classmethod
    def get_user_by_email(cls,data): 
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        if len(result) < 1: 
            return False
        return cls(result[0])
    
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result[0]

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(User.DB).query_db(query,user)
        if len(result) >= 1:
            flash("Email already taken.","register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address!","register")
            is_valid = False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.","register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.","register")
            is_valid = False
        if not PASS_REGEX.match(user['password']):
            flash("Password must be at least 8 characters.","register")
            is_valid = False
        if user['password'] != user['password_confirm']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid