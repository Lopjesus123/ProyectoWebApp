from django.urls import path
from ProyectoWebApp import views
from . import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
]
