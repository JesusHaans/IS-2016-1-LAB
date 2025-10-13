from django.db import models

# Create your models here.

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    publicado = models.DateField()

    def __str__(self):
        cadena = self.nombre + " de " + self.autor
        return cadena
