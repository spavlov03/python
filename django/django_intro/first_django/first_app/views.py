from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
# Create your views here.
def root(request): 
    return redirect('/blogs')
def index(request): 
    return HttpResponse("placeholder to later dispaly a list of all blogs")
def create(request):
    return redirect('/')
def show(request,number): 
    return HttpResponse("placeholder to display blog number: "+number)
def edit(request,number):
    return HttpResponse('placeholder to edit blog '+number)
def destroy(request,number): 
    return redirect('/blogs')
def json(request):
    return JsonResponse({'title' : "My first blog",'content' : "Lorem, ipsum dolor sit amet consectetur adipisicing elit."})
    