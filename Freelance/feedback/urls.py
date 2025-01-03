from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_index, name='feedback_index'),
]
