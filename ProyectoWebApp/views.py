from django.shortcuts import render, HttpResponse

# from .models import Auto

# Create your views here.


def home(request):

    return render(request,"ProyectoWebApp/home.html")

