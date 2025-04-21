from django.db import models

# Create your models here.

from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    #imagen = models.ImageField(upload_to='autos/')  # Asegúrate de tener Pillow instalado

