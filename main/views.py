from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

from .forms import CreateUserForm
from .models import *


def index(request):
    return render(request, 'main/Index.html',{})

@login_required(login_url='login')
def details_Lines(request):
    lines = Line.objects.order_by('-idCentral')
    # centrals = Central.objects.all()
    context = {
        # 'centrals': centrals, 
        'lines': lines
    }    
    return render(request, 'main/DetailsLines.html', context)

@login_required(login_url='login')
def details_Cabinets(request):
    cabinets = Cabinet.objects.order_by('-idAccumulations')
    # centrals = Central.objects.all()
    context = {
        # 'centrals': centrals, 
        'cabinets': cabinets
    }    
    return render(request, 'main/DetailsCabinets.html', context)

@login_required(login_url='login')
def details_Pylons(request):
    pylons = Pylon.objects.order_by('-idLine')
    # centrals = Central.objects.all()
    context = {
        # 'centrals': centrals, 
        'pylons': pylons
    }    
    return render(request, 'main/DetailsPylons.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('/main/index')
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

def logout_page(request):
    logout(request)
    return redirect('login')
    
# Create your views here.
