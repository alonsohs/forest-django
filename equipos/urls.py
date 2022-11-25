from django.urls import path

# from django.conf.url import url

from . import views

urlpatterns = [
    path('', views.equipos, name='equipos'),
    path('crear_equipo/', views.crearEquipo, name='crear_equipo'),
    # path('editar/<pk>', views.editarArbol, name='editar_arbol'),
    # path('eliminar/<pk>', views.eliminarArbol, name='eliminar_arbol'),
    path('agregar_miembro/<pk>', views.crearPersona, name='crear_persona')
]
