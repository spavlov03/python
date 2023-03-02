from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
import bcrypt   

# Create your views here.
def root(request): 
    return render(request,'index.html')
def register(request): 
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/users')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        logged_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
        context = {
            'user':logged_user
        }
    return redirect('/shows',context)
def login(request): 
    user = User.objects.filter(email=request.POST['email'])
    if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/shows')
    return redirect('/admin')