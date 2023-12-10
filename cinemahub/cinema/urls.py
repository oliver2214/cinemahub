from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("addmovie/", views.addmovie, name="addmovie"),
    path("login/", views.login, name="login"),
    path("movie/<int:id>", views.movie, name="movie"),
    path("movies/", views.movies, name="movies"),
    path("actor/<int:id>", views.actor, name="actor"),
    path("actors/", views.actors, name="actors"),
]
