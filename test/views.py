from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'test/Index.html',{})

def details(request):    
    return render(request, 'test/Details.html',{})
    
def login(request):
    return render(request, 'test/Login.html',{})

def register(request):
    return render(request, 'test/Register.html',{})
# Create your views here.
