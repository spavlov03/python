from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User

# Create your views here.
def root(request): 
    return render(request,'index.html')
def register(request): 
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/users')
    return redirect('/shows')