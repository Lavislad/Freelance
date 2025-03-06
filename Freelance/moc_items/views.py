import requests
from django.shortcuts import render


def moc_index(request):
    response = requests.get("http://localhost:8001/moc")

    if response.status_code == 200:
        data = response.json()
    else:
        data = None

    return render(request, "moc_items/moc_items.html", {"data": data})
