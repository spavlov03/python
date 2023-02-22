from django.shortcuts import render, redirect

# Create your views here.
def index(request): 
    
    if 'counter' in request.session: 
        print('key exists!')
        request.session['counter'] += 1
    else: 
        print("Key Counter does not exist")
        request.session['counter'] = 0 
    return render(request,'index.html')
def clear_ses(request): 
    del request.session['counter']
    return redirect('/')
def double(request): 
    request.session['counter'] += 1
    return redirect('/')
def custom(request):
    qty = int(request.POST['qty'])
    
    request.session['counter'] = request.session['counter'] + qty-1
    return redirect('/')