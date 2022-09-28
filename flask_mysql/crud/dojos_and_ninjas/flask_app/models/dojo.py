from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo: 
    DB = "dojosninjas"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.DB).query_db(query)
        #print("__ALL DOJOS__", results)
        dojos = []
        for row in results: 
            dojos.append(cls(row))
        return dojos
    @classmethod
    def new_dojo(cls,data): 
        query = "INSERT INTO dojos (name) VALUES (%(dojo_name)s)"
        results = connectToMySQL(cls.DB).query_db(query,data)
        print("___ADDING NEW DOJO__",results)
        return results
    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query,data)
        #print("ALL NINJASSSSS",results)
        dojo = cls(results[0])
        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(ninja) )
        return dojo 
