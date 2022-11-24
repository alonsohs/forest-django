from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from .forms import EquipoForm
from .models import Equipo, Persona


@login_required()
def equipos(request):
    equipos = Equipo.objects.all()
    personas = Persona.objects.all()
    contexto = {
        'equipos': equipos,
        'personas': personas
    }
    return render(request, 'equipos.html', contexto)


# Vistas basadas en funciones
# @login_required()
# def crearEquipo(request):
#     if request.method == 'POST':
#         form = EquipoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('equipos')
#     else:
#         form = EquipoForm()
#     return render(request, 'crear_arbol.html', {'form': form})
#
#
# @login_required()
# def editarEquipo(request, pk):
#     arbol = Equipo.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = EquipoForm(instance=arbol)
#     else:
#         form = EquipoForm(request.POST, instance=arbol)
#         if form.is_valid():
#             form.save()
#         return redirect('equipos')
#     return render(request, 'crear_arbol.html', {'form': form})
#
#
# @login_required()
# def eliminarEquipo(request, pk):
#     arbol = Equipo.objects.get(pk=pk)
#     arbol.delete()
#     return redirect('equipos')
