from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

def index(request):
    return render(request, 'test/Index.html',{})

def details(request):    
    return render(request, 'test/Details.html',{})

def login(request):
    return render(request, 'test/Login.html',{})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    # form = UserCreationForm()

    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    
    context = {'form':form}
    return render(request, 'test/Register.html', context)

def logout_view(request):
    logout(request)
    
# Create your views here.
