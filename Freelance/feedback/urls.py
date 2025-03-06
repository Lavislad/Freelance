from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_index, name='feedback_index'),
    path('<int:pk>', views.FeedbackDetailView.as_view(), name='feedback_details'),
    path('<int:pk>/update', views.FeedbackUpdateView.as_view(), name='feedback_update'),
    path('<int:pk>/delete', views.FeedbackDeleteView.as_view(), name='feedback_delete'),
    path('create_feedback', views.create_feedback, name='create_feedback')
]
