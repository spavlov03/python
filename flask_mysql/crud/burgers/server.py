from flask_app.controllers import burgers
from flask_app import app 



if __name__=="__main__":
    app.run(debug=True,port=8000)