from django.shortcuts import render


def news_index(request):
    data = {
        'title': 'News Page'
    }
    return render(request, 'news/news_index.html', data)
