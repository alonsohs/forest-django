from django.db import models

from generales.models import claseModelo

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    
    # Se sugiere nombra la clase en singular
    # No se deben indicar los clampos clave,
    # Django genera en automatico las PrimaryKey
    # AGREGAR UN ATRIBUTO "IDENTIFICADOR"
    
    def __str__(self):
        return '%s' % (self.nombre)

class Producto(claseModelo):
    descripcion = models.CharField(max_length=50) 
    precio = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    # AGERGAR LOS ATRIBUTOS "precio_compra" Y "precio_venta"
    def __str__(self):
        return (self.descripcion)