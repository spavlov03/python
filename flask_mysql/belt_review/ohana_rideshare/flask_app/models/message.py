from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ride,user,message

class Message: 
    DB = "ohana_rideshares"

    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.ride_id = data['ride_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def send_message(cls,data): 
        #print("SEND MSG QUERY DATA",data)
        query = "INSERT INTO messages (content,ride_id,sender_id,receiver_id) VALUES (%(content)s,%(ride_id)s,%(sender_id)s,%(receiver_id)s);"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def get_all_messages_for_ride(cls,data):
        #print("DATA INSIDE MSG QUERY is",data)
        query = "SELECT * FROM messages WHERE ride_id=%(ride_id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("GET ALL MSG QUERY",result)
        return result 