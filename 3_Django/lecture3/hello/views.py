from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")


def brian(request):
    return HttpResponse("Hello, Brian")


def david(request):
    return HttpResponse("Hello, David")
