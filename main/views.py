from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина'
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина',
        'about': 'Мы лучшие в своем деле!)'
    }
    return render(request, 'main/about.html', context)
