from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def root(request): 
    return render(request,'index.html')
def register(request):
    print(request.POST)
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        logged_user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
        request.session['logged_user_id'] = logged_user.id
        return redirect('/success')
def login(request):
    print("Before User")
    user = User.objects.filter(email=request.POST['email'])
    print("After User",user)
    if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['logged_user_id'] = logged_user.id
            print("Pass is good!")
            return redirect('/success')
    else:
        print("No User")
        messages.warning(request,"Invalid Email/Password")
        return redirect('/')
def success(request):
        context = {
            'logged_user' : User.objects.get(id=request.session['logged_user_id'])
        }
        return render(request,'home.html',context)
def logout(request):
    try :
        del request.session['logged_user_id']
    except KeyError:
        return redirect('/')