from django.shortcuts import render, HttpResponse
from .models import Auto

# Create your views here.


def home(request):

    return render(request,"ProyectoWebApp/home.html")


def autos_disponibles(request):
    marca_filtrada = request.GET.get('marca')
    if marca_filtrada:
        autos = Auto.objects.filter(marca=marca_filtrada)
    else:
        autos = Auto.objects.all()
    return render(request, "ProyectoWebApp/autos_disponibles.html", {"autos": autos})


def servicios(request):

    return render(request,"ProyectoWebApp/servicios.html")

def blog(request):

    return render(request,"ProyectoWebApp/blog.html")

def sobre_nostros(request):

    return render(request,"ProyectoWebApp/sobre_nosotros.html")

def contacto(request):

    return render(request,"ProyectoWebApp/contacto.html")