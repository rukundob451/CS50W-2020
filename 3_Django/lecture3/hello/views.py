from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from . import views


def index(request):
    return HttpResponse('Hello, world!')
