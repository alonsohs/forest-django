from django.urls import path

# from django.conf.url import url

from . import views

urlpatterns = [
    path('', views.proyectos, name='lista_proyectos'),
    path('crear/', views.crearProyecto, name='crear_proyecto'),
    path('<pk>', views.detalleProyecto, name='detalle_proyecto'),
    # path('eliminar/<pk>', views.eliminarArbol, name='eliminar_arbol'),
]
