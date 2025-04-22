from django.db import models

# Create your models here.


from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Auto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='autos/')
    disponible = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
