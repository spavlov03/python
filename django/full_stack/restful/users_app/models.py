from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self,postData): 
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name should be at least 1 characters"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name should be at least 1 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address'
        return errors

class User(models.Model): 
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()