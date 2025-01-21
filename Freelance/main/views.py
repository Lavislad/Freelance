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
