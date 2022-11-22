from django.urls import path

# from django.conf.url import url

from . import views

urlpatterns = [
    path('', views.equipos, name='equipos'),
    # path('crear/', views.crearArbol, name='crear_arbol'),
    # path('editar/<pk>', views.editarArbol, name='editar_arbol'),
    # path('eliminar/<pk>', views.eliminarArbol, name='eliminar_arbol'),
]
