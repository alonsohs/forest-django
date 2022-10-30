from django.contrib import admin

from .models import Categoria, Producto

# Register your models here.
class Categoria_Admin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    
admin.site.register(Categoria, Categoria_Admin)


class Producto_Admin(admin.ModelAdmin):
    list_display = ('descripcion', 'precio', 'categoria')
    
admin.site.register(Producto, Producto_Admin)