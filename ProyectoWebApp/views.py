from django.shortcuts import render, HttpResponse
from .models import Auto

# Create your views here.


def home(request):

    return render(request,"ProyectoWebApp/home.html")


def autos_disponibles(request):

    return render(request,"ProyectoWebApp/autos_disponibles.html")


def servicios(request):

    return render(request,"ProyectoWebApp/servicios.html")

def blog(request):

    return render(request,"ProyectoWebApp/blog.html")

def contacto(request):

    return render(request,"ProyectoWebApp/contacto.html")