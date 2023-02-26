from django.shortcuts import render,HttpResponse, redirect
from .models import User
# Create your views here.
def register(request): 
    return HttpResponse('placeholder for users to create a new user record')
def login(request): 
    return HttpResponse('placeholder for users to log in')
def users(request):
    context = { 
        "all_users":
        User.objects.all()
    }
    return render(request,'main.html',context)
def root(request): 
    return redirect('/blogs')