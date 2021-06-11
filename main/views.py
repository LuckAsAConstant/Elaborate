from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .forms import CreateUserForm
from .models import *


def index(request):
    return render(request, 'main/Index.html',{})

def details(request):
    centrals = Central.objects.all()
    context = {'centrals': centrals}    
    return render(request, 'main/Details.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('index')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, 'main/Login.html',{})

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'main/Register.html', context)

def logout(request):
    logout(request)
    return redirect('login')
    
# Create your views here.
