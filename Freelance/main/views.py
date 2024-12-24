from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse('<h4>Страница про нас</h4>')

def news(request):
    return HttpResponse('<h4>Страница новостей</h4>')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')
