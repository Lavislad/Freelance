# from django.contrib.gis.gdal.prototypes.srs import from_user_input
from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import DetailView, UpdateView, DeleteView

def feedback_index(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_index')
        else:
            error = 'Form is invalid'
    feedback = Feedback.objects.all
    form = FeedbackForm()
    data = {
        'title': 'Feedback Page',
        'feedback': feedback,
        'form': form,
        'error': error
    }
    return render(request, 'feedback/feedback_index.html', data)
