from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Message:
    DB = "private_wall"

    def __init__(self,data): 
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def send_message(cls,message_data):
        query = "INSERT INTO messages (content,user_id) VALUES (%(content)s,%(user_id)s);"
        result = connectToMySQL(cls.DB).query_db(query,message_data)
        print("___ADDING NEW USER___",result)
        return result