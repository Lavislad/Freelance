from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_index, name='news_index'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete')
]
