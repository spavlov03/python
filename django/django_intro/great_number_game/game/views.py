from django.shortcuts import render,redirect
import random

# Create your views here.
def index(request):
    request.session['number'] = random.randint(1,100)
    print(request.session['number'])
    request.session['counter'] = 0
    return render(request,'index.html')
def check(request): 
    print("Guessed number is ",request.POST['number'])
    if request.session['counter'] == 5 : 
        request.session['status'] = "you loose"
    else:
      if int(request.POST['number']) > request.session['number']:
          request.session['status'] = 'too high'
          request.session['counter'] += 1
      elif int(request.POST['number']) < request.session['number']:
          request.session['status'] = 'too low'
          request.session['counter'] += 1
      else : 
          request.session['status'] = 'match'
    
    return redirect('/result')
def result(request): 
    return render(request,'index.html')
def reset(request): 
    del request.session['number']
    del request.session['status']
    return redirect('/')