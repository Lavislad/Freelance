from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
