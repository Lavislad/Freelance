# from django.contrib.gis.gdal.prototypes.srs import from_user_input
from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Feedback
from .forms import FeedbackForm
from django.views.generic import DetailView, UpdateView, DeleteView

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'feedback/feedback_details.html'
    context_object_name = 'feedback'

class FeedbackUpdateView(UpdateView):
    model = Feedback
    template_name = 'feedback/feedback_update.html'
    form_class = FeedbackForm
    context_object_name = 'feedback'

class FeedbackDeleteView(DeleteView):
    model = Feedback
    template_name = 'feedback/feedback_delete.html'
    success_url = '/feedback/'
    context_object_name = 'feedback'

def feedback_index(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_index')
        else:
            error = 'Form is invalid'
    feedback = Feedback.objects.order_by('-date')
    form = FeedbackForm()
    data = {
        'title': 'Feedback Page',
        'feedback': feedback,
        'form': form,
        'error': error
    }
    return render(request, 'feedback/feedback_index.html', data)
