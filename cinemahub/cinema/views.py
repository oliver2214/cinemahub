from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


menu = [{"title": "CinemaHub", "url_name": "home"},
                 {"title": "О нас", "url_name": "about"},
                 {"title": "Добавить фильм", "url_name": "addmovie"},
                 {"title": "Войти", "url_name": "login"},
                 {"title": "Фильмы", "url_name": "movies"},
                 {"title": "Актёры", "url_name": "actors"}]


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found: 404</h1>")


def home(request):
    data = {
        "menu": menu
    }
    return render(request, "cinema/home.html", context=data)


def about(request):
    return HttpResponse("Страница сайта cinemahub О нас")


def addmovie(request):
    return HttpResponse("Страница сайта cinemahub Добавить фильм в медиатеку")


def login(request):
    return HttpResponse("Страница сайта cinemahub Авторизация")


def movie(request, id):
    data = {
        "id": id
    }
    return render(request, "cinema/movie.html", context=data)


def movies(request):
    data = {
        "title": "Список фильмов",
        "menu": menu,
        "movies": [
            {"id": 1, "title": "Fast&Furious", "genre": "боевик", "description": "Описание фильма Форсаж", "year": 2001},
            {"id": 2, "title": "American Pie", "genre": "комедия", "description": "Описание фильма Американский пирог", "year": 1999},
            {"id": 3, "title": "Зеленая миля", "genre": "драма", "description": "Описание фильма Зеленая миля", "year": 1999},
            {"id": 4, "title": "1+1", "genre": "драма", "description": "Описание фильма 1+1", "year": 2011}
              ]
    }

    return render(request, "cinema/movies.html", context=data)


def actor(request, id):
    data = {
        "id": id
    }
    return render(request, "cinema/actor.html", context=data)


def actors(request):
    data = {
        "title": "Актеры",
        "menu": menu,
        "actors": [
                {"id": 1, "name": "Vin Diesel", "birth_year": 1967, "nationality": "American"},
                {"id": 2, "name": "Paul Walker", "birth_year": 1973, "nationality": "American"},
                {"id": 3, "name": "Michelle Rodriguez", "birth_year": 1978, "nationality": "American"},
                {"id": 4, "name": "Jordana Brewster", "birth_year": 1980, "nationality": "American"},
                {"id": 5, "name": "Rick Yune", "birth_year": 1971, "nationality": "American"},
                {"id": 6, "name": "Jason Biggs", "birth_year": 1978, "nationality": "American"},
                {"id": 7, "name": "Chris Klein", "birth_year": 1979, "nationality": "American"},
                {"id": 8, "name": "Thomas Ian Nicholas", "birth_year": 1980, "nationality": "American"},
                {"id": 9, "name": "Eddie Murphy", "birth_year": 1961, "nationality": "American"},
                {"id": 10, "name": "Tom Hanks", "birth_year": 1956, "nationality": "American"},
                {"id": 11, "name": "Omar Sy", "birth_year": 1978, "nationality": "French"},
                {"id": 12, "name": "François Cluzet", "birth_year": 1955, "nationality": "French"}]
    }

    return render(request, "cinema/actors.html", context=data)
