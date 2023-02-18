from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
def index(request):
    return HttpResponse("Ko stana veeeee this is the equivalent of @app.route('/')!")
def one_method(request):                # no values passed via URL
    return HttpResponse("bears one method")                                
    
def another_method(request, my_val):	# my_val would be a number from the URL
    return HttpResponse("bears another method")    # given the example above, my_val would be 23
    
def yet_another(request, name):	        # name would be a string from the URL
    return HttpResponse("bears yet another method")                                # given the example above, name would be 'pooh'
    
def one_more(request, id, color): 	# id would be a number, and color a string from the URL
    return HttpResponse("one another method") 
def another_method(request):
    return redirect("/redirected_route")
def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})