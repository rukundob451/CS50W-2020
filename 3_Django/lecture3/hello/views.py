from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.(
# def index(request):
#    return HttpResponse("Hello world!")

def index(request):
    return render(request, "hello/index.html")


def ira(request):
    return HttpResponse("Hello Ira!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.upper()}!")
