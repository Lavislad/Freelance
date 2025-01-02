from django.shortcuts import render
from .models import Articles

def news_index(request):
    news = Articles.objects.order_by('-date')
    data = {
        'title': 'News Page',
        'news': news
    }
    return render(request, 'news/news_index.html', data)
