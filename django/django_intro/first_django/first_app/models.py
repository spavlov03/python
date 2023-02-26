from django.db import models

# Create your models here.
from users.models import User
# Create your models here.
class Blog(models.Model): 
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,related_name='blogs',on_delete=models.CASCADE)