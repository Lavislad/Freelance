from django.shortcuts import render
from .models import Feedback

def feedback_index(request):
    feedback = Feedback.objects.all()
    data = {
        'title': 'Feedback Page',
        'feedback': feedback
    }
    return render(request, 'feedback/feedback_index.html', data)
