from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import EquipoForm, PersonaForm
from .models import Equipo, Persona


@login_required()
def equipos(request):
    personas = Persona.objects.all()
    equiposObject = Equipo.objects.all()

    equipos = {}
    for equipo in equiposObject:
        equipos[equipo.id] = {
            'nombre': equipo.nombre,
            'personas': []
        }

    for persona in personas:
        if equipos[persona.equipo.id] != None:
            equipos[persona.equipo.id]['personas'].append(persona)

    print(equipos)
    equipoCtx = []
    for equipo in equipos:
        formatoEquipo = {
            'id': equipo,
            'nombre': equipos[equipo]['nombre'],
            'personas': equipos[equipo]['personas']
        }
        equipoCtx.append(formatoEquipo)

    contexto = {
        'equipos': equipoCtx,
    }

    return render(request, 'equipos.html', contexto)


@login_required()
def crearEquipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipos')
    else:
        form = EquipoForm()
    return render(request, 'crear_equipo.html', {'form': form})

@login_required()
def crearPersona(request, pk):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('equipos')
    else:
        form = PersonaForm(initial={'equipo': pk})
    return render(request, 'crear_persona.html', {'form': form})
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
