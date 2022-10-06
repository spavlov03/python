from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASS_REGEX = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$")

#Minimum 8 characters - {8,}
#At least one uppercase - (?=.*?[A-Z])
#At least one lowercase - (?=.*?[a-z])
#At least one digit - (?=.*?[0-9])
#At least one special character - (?=.*?[#?!@$%^&*-])

class User:
    DB = "private_wall"

    def __init__(self,data): 
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def register(cls,user_data):
        data = {
            "first_name":user_data['first_name'],
            "last_name":user_data['last_name'],
            "email":user_data['email'],
            "password":bcrypt.generate_password_hash(user_data['password'])
        }
        query = "INSERT INTO users (first_name,last_name,email,password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("___ADDING NEW USER___",result)
        return result

    @classmethod
    def get_user_info(cls,data):
        #print("DATA IS --- ",data)
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        users = []
        for row in results:
            users.append(cls(row))
        #print("__SELECTING USER__",result)
        return users
    @classmethod
    def get_user_info_by_email(cls,email):
        data = {"email":email}
        query = "SELECT * FROM users WHERE email= %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        if len(result) == 0:
            return False
        else:
            return cls(result[0])
    @classmethod
    def get_user_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return cls(result[0])

    @staticmethod
    def validate_register(user):
        is_valid = True
        user_in_db = User.get_user_info_by_email(user['email'])
        print("USER IN DB",user_in_db)
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters.","register")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters.","register")
            is_valid = False
        if len(user['email']) == 0 or not EMAIL_REGEX.match(user['email']):
            flash("Invalid email.","register")
            is_valid = False
        if user_in_db is not False:
            flash("email is already in use!","register")
            is_valid = False
        if not PASS_REGEX.match(user['password']):
            flash("Password must be at least 8 characters and include One Uppercase, One lowercase and a number","register")
            is_valid = False
        if user['password'] != user['password_confirm']:
            flash("Passwords don't match","register")
            is_valid = False
        return is_valid
    @staticmethod
    def validate_login(user):
        is_valid = True
        user_in_db = User.get_user_info_by_email(user['email'])
        print("USER IN DB",user_in_db)
        if len(user['email']) == 0 or not EMAIL_REGEX.match(user['email']):
            flash("Invalid email.","login")
            is_valid = False
        if user_in_db is not False:
            flash("wrong email/password","register")
            is_valid = False
        if len(user['password']) < 8 or not bcrypt.check_password_hash(user_in_db.password,user['password']):
            flash("wrong email/password","register")
            is_valid = False
        if is_valid:
            return user_in_db
        else:        
            return is_valid