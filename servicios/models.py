from django.db import models

# Create your models here.

class Servicios(models.Model):  # Usa mayúscula si es el nombre de la clase (por convención)
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'servicios'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo

