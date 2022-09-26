"""
main folder
    flask_app
        config
            mysqlconnection.py
        controllers
            routes, session
        models
            class for instances
            do the queries
        static
            css
                style.css
            javascript
                script.js
        templates
            all html
        __init__.py
            from flask import Flask
            app = Flask(__name__)
            app.secret_key = "shhhhhh"
    server.py
        from flask_app import app

Model
    May build database tables
    Handles logic that relies on data
    Interfaces with the database
View
    HTML page that gets served to the client
    May contain some logic to be handled by a template engine   
Controller
    Receives incoming requests
    Minimal logic
    Calls on models to aggregate/process data
    Determines appropriate response







"""