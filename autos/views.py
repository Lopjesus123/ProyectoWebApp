from django.shortcuts import render

# Create your views here.



def autos_disponibles(request):
    return render(request, "autos/autos_disponibles.html")

