from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Message:
    DB = "private_wall"

    def __init__(self,data): 
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sender_id = data['sender_id']
        self.receiver_id = data['receiver_id']
        self.creator = None

    @classmethod
    def send_message(cls,message_data):
        query = """
        INSERT INTO messages (content,sender_id,receiver_id) VALUES (%(content)s,%(sender_id)s,%(receiver_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query,message_data)
        print("SENDING NEW MESSAGE___",result)
        # user.User.messages = result
        # print("USERS msgs",user.User.messages)
        return result
    @classmethod
    def get_all_messages_for_user(cls,user_id):
        query = """
        SELECT * FROM messages 
        JOIN users ON messages.sender_id = users.id
        WHERE receiver_id = %(receiver_id)s ORDER BY messages.created_at DESC;
        """
        result = connectToMySQL(cls.DB).query_db(query,user_id)
        # print(f"GETTING all messages for user - {user_id}",result)
        messages = []
        for row in result:
            message = cls(row)
            message_creator = {
                "id":row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            creator = user.User(message_creator)
            message.creator = creator
            messages.append(message)
        return messages

    @classmethod
    def get_all_messages_by_user(cls,user_id):
        query = """
        SELECT * FROM messages WHERE sender_id = %(sender_id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,user_id)
        print("")
        
        return result

    @classmethod
    def message_delete(cls,data):
        query = "DELETE FROM messages WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result