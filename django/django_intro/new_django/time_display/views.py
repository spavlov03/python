from django.shortcuts import render
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