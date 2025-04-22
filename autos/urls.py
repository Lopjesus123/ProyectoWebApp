from django.urls import path

from .import views


urlpatterns = [

    path('', views.autos_disponibles, name="autos_disponibles"),
]

