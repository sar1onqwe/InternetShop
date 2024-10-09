from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



def index(request):

    context = {
        'title': 'Главная страница',
        'content': 'Главная страница магазина',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'content': 'Главная страница магазина',
        'about': 'Мы лучшие в своем деле!)'
    }
    return render(request, 'main/about.html', context)
