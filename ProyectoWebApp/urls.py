from django.urls import path


from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('autos-disponibles/', views.autos_disponibles, name="autos_disponibles"),
    path('servicios/', views.servicios, name="servicios"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
