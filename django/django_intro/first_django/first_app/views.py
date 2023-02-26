from django.shortcuts import render, redirect, HttpResponse
from .models import Blog
# Create your views here.
def index(request): 
    context = {'blogs':Blog.objects.all()}
    return render(request,'index.html',context)
def new(request): 
    return HttpResponse("placeholder to display a new form to create a new blog")
def create(request):
    return redirect('/blogs')
def show(request,number): 
    return HttpResponse("placeholder to display blog number: "+number)
def edit(request,number):
    return HttpResponse('placeholder to edit blog '+number)
def destroy(request,number): 
    return redirect('/blogs')

    