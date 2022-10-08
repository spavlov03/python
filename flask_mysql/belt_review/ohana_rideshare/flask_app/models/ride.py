from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import ride,user

class Ride: 
    DB = "ohana_rideshares"

    def __init__(self,data): 
        self.id = data['id']
        self.destination = data['destination']
        self.pick_up_location = data['pick_up_location']
        self.rideshare_date = data['rideshare_date']
        self.details = data['details']
        self.user_id = data['user_id']
        self.driver_id = data['driver_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def request_ride(cls,data):
        query = "INSERT INTO rides (destination,pick_up_location,rideshare_date,details,user_id) VALUES (%(destination)s,%(pick_up_location)s,%(rideshare_date)s,%(details)s,%(user_id)s);"
        print("DATA BEFORE QUERY IS ----",data)
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("ADDING A NEW RIDE----",result)
        return result
    @classmethod
    def get_all_rides(cls):
        query = "SELECT * FROM rides JOIN users on rides.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        print("RESULTS ARE_-----",results)
        rides = []
        for row in results:
            ride = cls(row)
            rider_creator_info = {
                "id":row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['created_at'],
                "updated_at": row['updated_at']
            }
            creator = user.User(rider_creator_info)
            ride.creator = creator
            rides.append(ride)
        return rides
    @staticmethod
    def validate_ride(ride):
        is_valid = True
        if len(ride['destination']) < 3:
            flash("Destination must be at least 3 characters.","ride")
            is_valid = False
        if len(ride['pick_up_location']) < 3:
            flash("Pick up location must be at least 3 characters.","ride")
            is_valid = False
        if len(ride['details']) < 10:
            flash("Details must be at least 3 characters.","ride")
            is_valid = False
        return is_valid