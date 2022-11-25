from django.db import models

from arboles.models import Arbol
from equipos.models import Persona, Equipo

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    urlImagen = models.CharField(max_length=120, default='https://www.bbva.com/wp-content/uploads/2021/11/reforestacio%CC%81n_plantar-arboles-sostenibilidad-cuidado-medioambiente-planeta-bosques--1024x629.jpg')
    avance = models.IntegerField(null=True)
    fecha_inicio = models.DateField()
    fecha_limite = models.DateField()
    presupuesto_arboles = models.IntegerField(null=True, default=0)
    presupuesto = models.FloatField()
    material_disponible = models.IntegerField(null=True)

    ubicacion = models.TextField()
    lider = models.ForeignKey(Persona, on_delete=models.SET_NULL, blank=True, null=True)

    CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Pausa', 'Pausa'),
        ('Completado', 'Completado'),
    ]
    status = models.CharField(max_length=40, choices=CHOICES, default='Activo')

    SUELO_OPCIONES = [
        ('Sustrato', 'Sustrato'),
        ('Caliza', 'Caliza'),
        ('Cuarcita', 'Cuarcita'),
        ('Arcilla', 'Arcilla'),
        ('Turba', 'Turba'),
    ]
    tipo_suelo = models.CharField(max_length=30, choices=SUELO_OPCIONES)
    metros_cuadrados = models.FloatField()

    CLIMA_OPCIONES = [
        ('Frio', 'Frio'),
        ('Calido', 'Calido'),
        ('Humedo', 'Humedo'),
        ('Soleado', 'Soleado'),
        ('Seco', 'Seco'),
    ]
    clima = models.CharField(max_length=30, choices=CLIMA_OPCIONES)
    tipo_arbol = models.ForeignKey(Arbol,on_delete=models.SET_NULL, blank=True, null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)

    arboles_meta = models.IntegerField(default=0)
    arboles_platados = models.IntegerField(default=0)

    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return '%s' % (self.nombre)


