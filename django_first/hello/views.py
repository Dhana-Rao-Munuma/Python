from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhana(request):
    return HttpResponse("Hello Dhana!")

def index(request):
    return HttpResponse("Hello!")

def anna(request):
    return HttpResponse("Hello Anna!")

def greet(request, name):
    return HttpResponse(f"Hello {name.upper()}")

def index_render(request):
    return render(request, "hello/index_render.html")

def greet_render(request, name):
    return render(request,"hello/greet_render.html", {
        "name": name.upper()
    })