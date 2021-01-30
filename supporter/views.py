from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Helper/index.html', {'title': 'Главная страница'})
