from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import Show

# Create your views here.
def root(request): 
    return redirect('/shows')
def new(request): 
    return render(request,'add_show.html')
def add(request): 
    print(request.POST)
    this_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], description = request.POST['description'])
    return redirect(f'/shows/{this_show.id}')
def delete(request,id): 
    Show.objects.get(id=id).delete()
    return redirect('/shows')
def edit(request,id): 
    context = { 
        "show":Show.objects.get(id=id)
    }
    print("Date is ",context['show'].release_date)
    return render(request,"edit_show.html",context)
def edit_show(request,id): 
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect(f'/shows/{id}/edit')
    else:
        this_show = Show.objects.get(id=id)
        this_show.title = request.POST['title']
        this_show.network = request.POST['network']
        this_show.release_date = request.POST['release_date']
        this_show.description = request.POST['description']
        this_show.save()
        return redirect(f"/shows/{this_show.id}")
def show(request,id): 
    context = {
      "show" : Show.objects.get(id=id)}
    return render(request,'show.html',context)
def all(request): 
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request,'all_shows.html',context)