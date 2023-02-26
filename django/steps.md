Activate your environment:
    source djangoPy3Env/bin/activate 

With our Django virtual environment activated, create a new Django project. First navigate to where you want the project to be saved. Then run this command, specifying a project name of our choosing:
    django-admin startproject your_project_name_here

Run Project :
    python3 manage.py runserver

Create new app : 
    python3 manage.py startapp your_app_name_here

Add each app to settings.py in Project
add urls pat to main urls.py - path('',include("app.urls"))
Add urls.py to app folder 
    from django.urls import path
    from . import views
    urlpatterns = [
        path('',views.index)
    ]


Migrations - session: 
    python3 manage.py makemigrations
    
    python3 manage.py migrate
