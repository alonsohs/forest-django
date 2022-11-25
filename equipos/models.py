from django.db import models

from generales.models import claseModelo

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '%s' % (self.nombre)

class Persona(models.Model):
    urlImagen = models.CharField(max_length=150, default='https://icons.veryicon.com/png/o/internet--web/prejudice/user-128.png')
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    CHOICES = [
        ('Staff', 'Staff'),
        ('Supervisor', 'Supervisor'),
        ('Lider', 'Lider'),
        ('Coordinador', 'Coordinador'),
    ]
    rol = models.CharField(max_length=30, choices=CHOICES, default='Staff')
    equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, blank=True, null=True)



