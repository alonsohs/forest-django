from django.shortcuts import render, redirect
from django.http import HttpResponse

from catalogos.forms import ProductoForm
from .models import Categoria, Producto
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def home(request):
    return render(request, 'home.html')


def logout(request):
    logout(request)
    return redirect('/')



# CREACION DE LAS FUNCIONES PARA EL CRUD

# Vistas basadas en clases

class CreateProducto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy('listar_producto')

class ListProducto(ListView):
    model = Producto
    template_name = "listar_producto.html"

class UpdateProducto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "crear_producto.html"
    success_url = reverse_lazy('home')


# Vistas basadas en funciones
def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    else:
        form = ProductoForm()
    return render (request, 'crear_producto.html', {'form':form})

def listarProducto(request):
    productos = Producto.objects.all()
    contexto = {'productos': productos}
    return render (request, 'listar_producto.html', contexto)

def editarProducto(request,pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form=ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect ('home')
    return render (request, 'crear_producto.html', {'form' : form})

def categorias(request):
    # return render(request, 'categorias.html')

    # Uso de los Querysets de Django - consultas a la BD mediante el ORM
    categorias = Categoria.objects.all().order_by('id')
    contexto = {'categorias' : categorias}
    return render (request, 'categorias.html', contexto)

def productos(request):
    return render(request, 'productos.html')



