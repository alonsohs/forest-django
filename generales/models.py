from django.db import models

# Se crea UNA CLASE MODELO ABSTRACTA que se heredará a otros modelos
# en otras aplicaciones

class claseModelo(models.Model):
    activo = models.BooleanField(default=True)
    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True    