from django.db import models

# Create your models here.
class ShowManager(models.Manager): 
    def basic_validator(self,postData): 
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = "Show title should be at least 5 characters"
        if len(postData['description']) <10: 
            errors['description'] = 'Show description should be at least 10 characters'
        return errors
    
class Show(models.Model): 
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.CharField(max_length=45)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
