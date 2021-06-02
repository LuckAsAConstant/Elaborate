from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

def index(request):
    return render(request, 'main/Index.html',{})

def details(request):    
    return render(request, 'main/Details.html',{})

def login(request):
    return render(request, 'main/Login.html',{})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'main/Register.html', context)

def logout_view(request):
    logout(request)
    
# Create your views here.
