from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("Ko stana veeeee this is the equivalent of @app.route('/')!")