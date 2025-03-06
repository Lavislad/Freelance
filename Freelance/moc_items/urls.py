from django.urls import path

from . import views

urlpatterns = [
    path("", views.moc_index, name="moc_index"),
]
