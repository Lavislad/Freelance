from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    data = {
        'form': form
    }
    return render(request, 'account/login.html', data)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    data = {
        'form': form
    }
    return render(request, 'account/register.html', data)

def logout(request):
    auth.logout(request)
    return redirect('index')
