from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def root(request): 
    return render(request,'index.html')
def register(request):
    print(request.POST)
    # if User.objects.filter(email=request.POST['email']):
    #     print("Email Taken")
    #     messages.warning(request,"Email already taken")
    #     return redirect('/')
    # else:
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
    # print("Before User")
    user = User.objects.filter(email=request.POST['email'])
    # print("After User",user)
    if user: 
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['logged_user_id'] = logged_user.id
            # print("Pass is good!")
            return redirect('/success')
        else: 
            print('Wrong Pass')
            messages.warning(request,"Invalid Email/Password")
            return redirect('/')    
    else: 
        print("No User")
        messages.warning(request,"Invalid Email/Password")
        return redirect('/')
def success(request):
        if "logged_user_id" not in request.session:
            return redirect('/')
        else:
            context = {
                'logged_user' : User.objects.get(id=request.session['logged_user_id'])
            }
            return render(request,'home.html',context)
def logout(request):
    try :
        del request.session['logged_user_id']
        return redirect('/')
    except KeyError:
        return redirect('/')