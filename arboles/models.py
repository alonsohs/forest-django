from django.db import models

from generales.models import claseModelo


# Create your models here.
class Arbol(models.Model):
    urlImagen = models.CharField(max_length=150)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    ecosistema = models.CharField(max_length=30)
    nombreCientifico = models.CharField(max_length=50)
    altura = models.CharField(max_length=30)
    precio = models.FloatField()
    metrosCuadrados = models.FloatField()

    def __str__(self):
        return '%s' % (self.nombre)

