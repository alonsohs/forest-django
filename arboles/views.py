from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ArbolForm
from .models import Arbol


@login_required()
def arboles(request):
    arboles = Arbol.objects.all()
    contexto = {'arboles': arboles}
    return render(request, 'arboles.html', contexto)


# Vistas basadas en funciones
@login_required()
def crearArbol(request):
    if request.method == 'POST':
        form = ArbolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('arboles')
    else:
        form = ArbolForm()
    return render(request, 'crear_arbol.html', {'form': form})


@login_required()
def editarArbol(request, pk):
    arbol = Arbol.objects.get(pk=pk)
    if request.method == 'GET':
        form = ArbolForm(instance=arbol)
    else:
        form = ArbolForm(request.POST, instance=arbol)
        if form.is_valid():
            form.save()
        return redirect('arboles')
    return render(request, 'crear_arbol.html', {'form': form})


@login_required()
def eliminarArbol(request, pk):
    arbol = Arbol.objects.get(pk=pk)
    arbol.delete()
    return redirect('arboles')

