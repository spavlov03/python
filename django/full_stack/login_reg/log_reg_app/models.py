from django.db import models
import re
import datetime
from datetime import timedelta


# Create your models here.
class UserManager(models.Manager):
    def validator(self,postData):
        print("Inside Validator ")
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if postData['bday'] > str(datetime.date.today() - timedelta(4745)):
            print("Too Young!")
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
        if User.objects.filter(email=postData['email']):
            print("Email Taken")
            errors['email'] = "Email already taken"
        if postData['password'] != postData['password_conf']: 
            errors['password'] = 'Passwords must match'
        if len(postData['password']) < 8:
            errors['last_name'] = "Password should be at least 8 characters"
        return errors

  
class User(models.Model): 
    objects = UserManager()
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)