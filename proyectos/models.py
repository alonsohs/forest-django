from django.db import models

class Proyectos(models.Model):
    urlImagen = models.CharField(max_length=150, default='https://icons.veryicon.com/png/o/internet--web/prejudice/user-128.png')
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    lugar = models.CharField(max_length=30)
    latitud = models.CharField(max_length=30)
    altitud = models.CharField(max_length=30)
    metrosCuadrados = models.CharField(max_length=30)
   