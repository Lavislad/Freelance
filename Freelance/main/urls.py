from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vacancies', views.vacancy_list, name='vacancy_list'),
    path('create_a_vacancy', views.vacancy_create, name='vacancy_create'),
]
