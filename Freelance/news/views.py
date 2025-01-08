from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def news_index(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_index')
        else:
            error = 'Form is invalid'
    news = Articles.objects.order_by('-date')
    form = ArticlesForm()
    data = {
        'title': 'News Page',
        'news': news,
        'form': form,
        'error': error
    }
    return render(request, 'news/news_index.html', data)
