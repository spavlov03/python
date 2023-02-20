from django.shortcuts import render,redirect
from time import gmtime,strftime
from datetime import datetime
import pytz
# Create your views here.
def index(request):
    context = {
        # "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
        'time': datetime.now(pytz.timezone('America/Los_Angeles')).strftime('%H:%M'),
        'date': datetime.now().strftime('%b %d, %Y')
    }
    return render(request,'index.html',context)
def form(request): 
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
    return render(request,'form.html')
def form_result(request): 
    print(request)
    return redirect("/")