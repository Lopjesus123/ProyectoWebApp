from django.shortcuts import render, HttpResponse

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


def contacto(request):

    return render(request,"ProyectoWebApp/contacto.html")