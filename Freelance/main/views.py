from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancy, Tags


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
    tag_slug = request.GET.get('tag')
    vacancies = Vacancy.objects.all().prefetch_related('tags')
    all_tags = Tags.objects.all()

    if tag_slug:
        vacancies = vacancies.filter(tags__title=tag_slug)

    data = {
        'vacancies': vacancies,
        'all_tags': all_tags,
        'current_tag': tag_slug,
    }
    return render(request, 'main/vacancy_list.html', data)
