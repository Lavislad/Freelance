from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('feedbacks', views.user_feedbacks, name='user_feedbacks'),
    path('vacancies', views.user_vacancies, name='user_vacancies'),
]
