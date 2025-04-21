from django.urls import path

from ProyectoWebApp import views


urlpatterns = [
    path('', views.home, name="home"),
    path('autos_disponibles/', views.autos_disponibles, name="autos_disponibles"),
    path('servicios/', views.servicios, name="servicios"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),
]
