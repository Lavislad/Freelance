from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Main Page',
        'values': ['Sime', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': '28'
        },
        'active': 'active'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return HttpResponse('<h4>Страница про нас</h4>')

def news(request):
    return HttpResponse('<h4>Страница новостей</h4>')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')
