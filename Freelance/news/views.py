from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

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
