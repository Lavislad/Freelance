from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancy, Tags
from django.db.models import Q


def index(request):
    data = {
        'title': 'Main Page',
        'active': 'active'
    }
    return render(request, 'main/index.html', data)

def vacancy_list(request):
    selected_tags = request.GET.getlist('tags')
    vacancies = Vacancy.objects.all().prefetch_related('tags').order_by('-date')
    all_tags = Tags.objects.all()

    if selected_tags:
        # q_objects = Q()
        for tag in selected_tags:
            vacancies = vacancies.filter(tags__title=tag).distinct()
        # vacancies = vacancies.filter(q_objects).distinct()

    data = {
        'vacancies': vacancies,
        'all_tags': all_tags,
        'selected_tags': selected_tags,
    }
    return render(request, 'main/vacancy_list.html', data)
