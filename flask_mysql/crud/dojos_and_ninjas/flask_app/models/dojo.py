from flask_app.config.mysqlconnection import connectToMySQL

class Dojo: 
    DB = "dojosninjas"

    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL(cls.DB).query_db(query)
        print("__ALL DOJOS__", results)
        dojos = []
        for row in results: 
            dojos.append(cls(row))
        return dojos
        