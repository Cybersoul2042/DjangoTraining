from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def amir(request):
    return HttpResponse("Hello, amir!!!")

def user(request, name):
    return render(request, "hello/user.html", {
        "name": name.capitalize() 
    })
