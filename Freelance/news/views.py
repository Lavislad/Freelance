from django.shortcuts import render
from .models import Articles

def news_index(request):
    news = Articles.objects.all()
    data = {
        'title': 'News Page'
    }
    return render(request, 'news/news_index.html', data)
