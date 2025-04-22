from django.shortcuts import render, HttpResponse
from servicios.models import Servicios


from .models import Auto #ignorar , si borra mama todo

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

    servicios=Servicios.objects.all()
    return render(request,"ProyectoWebApp/servicios.html", {"servicios": servicios} )

def blog(request):

    return render(request,"ProyectoWebApp/blog.html")

def contacto(request):

    return render(request,"ProyectoWebApp/contacto.html")