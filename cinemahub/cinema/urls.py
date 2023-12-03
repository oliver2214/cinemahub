from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("index/", views.index),
    path("get_cinema/<int:id>/", views.get_cinema_id),
    path("get_cinema/<slug:name>/", views.get_cinema_name),
    path("present/<slug:name>/<str:present>/", views.get_cinema_present)
]
