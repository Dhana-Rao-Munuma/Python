from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    Today=datetime.datetime.now()
    return render(request, "newyear/index.html", 
         {"newyear": Today.month == 1 and Today.day == 1 })