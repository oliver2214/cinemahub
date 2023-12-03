from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Ответ от cinema index")


def get_cinema_id(request, id):
    return HttpResponse(f"<h1>Фильма с id={id} нет</h1>")


def get_cinema_name(request, name):
    return HttpResponse(f"<h1>Фильма с name={name} нет")


def get_cinema_present(request, name, present):
    return HttpResponse(f"<h1>Фильма с name={name} нет</h1>\n<a>{present}</a>")
