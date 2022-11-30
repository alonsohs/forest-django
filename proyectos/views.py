from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from equipos.models import Persona
from proyectos.forms import ProyectoForm
from proyectos.models import Proyecto

from datetime import date

@login_required()
def proyectos(request):
    proyectos = Proyecto.objects.filter(user=request.user)
    contexto = {
        'proyectos': proyectos,
    }
    return render(request, 'lista_proyectos.html', contexto)


def crearProyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.user = request.user
            proyecto.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', {'form': form})


def detalleProyecto(request, pk):
    proyecto = Proyecto.objects.get(pk=pk)
    estadisticas = {}

    today = date.today()

    dias_restantes = (proyecto.fecha_limite - today).days

    estadisticas['dias'] = dias_restantes

    if proyecto.arboles_meta != 0:
        estadisticas['progreso'] = (proyecto.arboles_platados * 100) / proyecto.arboles_meta


    estadisticas['gastos'] = 10000

    equipo = Persona.objects.filter(equipo = proyecto.equipo)

    contexto = {
        'proyecto': proyecto,
        'estadisticas': estadisticas,
        'equipo_persona': equipo
    }
    return render(request, 'detalle_proyecto.html', contexto)