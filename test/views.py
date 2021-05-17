from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the test index.")

def details(request):
    # x = 5
    output = "<h1>Hello world, you're the details view:<h1>"
    return HttpResponse(output)

def login(request):

    return HttpResponse("Login view")

def register(request):
    
    return HttpResponse("Register")
# Create your views here.
