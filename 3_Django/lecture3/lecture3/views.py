from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest




def index(request):
    return HttpResponse('Hello, world!')
