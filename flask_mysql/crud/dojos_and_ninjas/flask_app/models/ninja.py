from flask_app.config.mysqlconnection import connectToMySQL

class Ninja: 
    DB = "dojosninjas"

    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def new_ninja(cls,data): 
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        #print("___ADDING NEW NINJA__",results)
        return results
    
    @classmethod
    def delete_ninja(cls,id):
        data = {"id":id}
        query = "DELETE FROM ninjas WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("___ DELETING NINJA ___",result)
        return result
    @classmethod
    def get_ninja_by_id(cls,id):
        data = {"id":id}
        query = "SELECT * FROM ninjas where id = %(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        #print("___SHOWING NINJA___",result)
        return result
    @classmethod
    def edit_ninja(cls,data):
        print("DATA IS ----",data)
        query = "UPDATE ninjas SET first_name=%(first_name)s,last_name=%(last_name)s,age=%(age)s WHERE id=%(id)s"
        result = connectToMySQL(cls.DB).query_db(query,data)
        print("___UPDATING NINJA___",result)
        return result

