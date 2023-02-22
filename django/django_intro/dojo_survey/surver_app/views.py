from django.shortcuts import render, redirect

# Create your views here.
def index(request): 
    return render(request,'index.html')
def create_user(request): 
    print('Got Post Info.....',request.POST)
    name = request.POST['name']
    request.session['name'] = name
    request.session['counter'] = 100
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    context = {
        'name' : name, 
        'location' : location, 
        'language': language, 
        'comment': comment,
    }
    return render(request,'result.html',context)
def result(request): 
    return render(request,'result.html')