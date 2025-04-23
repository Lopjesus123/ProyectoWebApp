from django.shortcuts import render
from .models import Auto

# Create your views here.



def autos_disponibles(request):

    autos = Auto.objects.all()
    return render(request, "autos/autos_disponibles.html", {"autos": autos})

