from django.shortcuts import render

task_entries = ["apple","banana","sapota"]

# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": task_entries
    })

def add(request):
    return(render(request, "tasks/add.html"))