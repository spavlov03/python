from time import strptime
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
        #print("DATA BEFORE QUERY IS ----",data)
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("ADDING A NEW RIDE----",result)
        return result
    @classmethod
    def get_all_rides(cls):
        query = "SELECT * FROM rides JOIN users on rides.user_id = users.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        #print("RESULTS ARE_-----",results)
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

    @classmethod
    def get_all_rides_with_drivers(cls):
        query = "SELECT * FROM rides JOIN users ON rides.user_id = users.id JOIN users AS drivers ON rides.driver_id = drivers.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        #print("RESULTS ARE_-----",results)
        rides = []
        for row in results:
            rides.append(row)
        #print("RIDES ARE ----",rides)
        return rides
    @classmethod
    def get_one_ride_with_drivers(cls,data):
        query = "SELECT * FROM rides JOIN users ON rides.user_id = users.id JOIN users AS drivers ON rides.driver_id = drivers.id WHERE rides.id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        #print("RESULTS ARE_-----",results)
        return results[0]

    @classmethod
    def get_ride_by_id(cls,data):
        query = "SELECT * FROM rides WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("GET RIDE BY ID RESULT----",result)
        return result [0]

    @classmethod
    def delete_ride(cls,data):
        query = "DELETE FROM rides WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("DELETING RIDE RESULT---",result)
        return result
    @classmethod
    def driver_add(cls,data): 
        query = "UPDATE rides SET driver_id = %(driver_id)s WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("ADDING DRIVER to RIDE",result)
        return result
    @classmethod
    def driver_remove(cls,id): 
        data = {"id": id}
        query = "UPDATE rides SET driver_id = NULL WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    @classmethod
    def edit_ride_by_id(cls,data):
        query = "UPDATE rides SET pick_up_location = %(pick_up_location)s, details = %(details)s WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("EDIT RIDE QUERY ----",result)
        return result

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
            flash("Details must be at least 10 characters.","ride")
            is_valid = False
        if len(ride['rideshare_date']) < 3:
            flash("Rideshare date must be YYYY-MM-DD format","ride")
            is_valid = False
        return is_valid