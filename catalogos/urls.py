from django.urls import path

# from django.conf.url import url

from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('categorias/',views.categorias, name='categorias'),
    path('productos/',views.productos, name='productos'),

    path('crear_producto/',views.crearProducto, name="crear_producto"),
    path('listar_producto/', views.listarProducto, name="listar_producto"),
    path('editar_producto/<pk>',views.editarProducto,name="editar_producto"),

    #url(r'^editar_producto/(?P<id>\d+)$',views.editarProducto,name="editar_producto"),

    # path('crear_producto/', CreateProducto.as_view(), name="crear_producto"),
    # path('listar_producto/', ListProducto.as_view(), name="listar_producto"),
    # path('editar_producto/<pk>',UpdateProducto.as_view(),name="editar_producto"),
    
]
