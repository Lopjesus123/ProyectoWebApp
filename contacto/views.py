from django.shortcuts import render

from .forms import FormularioContacto
# Create your views here.


def contacto(request):
    fromulario_contacto=FormularioContacto()
    return render(request,"contacto/contacto.html", {'miFormulario': fromulario_contacto})