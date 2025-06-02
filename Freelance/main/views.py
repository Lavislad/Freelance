from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vacancy, Tags
from .forms import VacancyForm
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

def vacancy_create(request):
    error = ''
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
            return redirect('vacancy_list')
        else:
            error = 'Form is invalid'
    else:
        form = VacancyForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/vacancy_create.html', data)
