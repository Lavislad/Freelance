from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancy


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

def vacancy_list(request):
    vacancies = Vacancy.objects.all().prefetch_related('tags')
    data = {
        'vacancies': vacancies,
    }
    return render(request, 'main/vacancy_list.html', data)
