from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required()
def proyectos(request):
    # equipos = Equipo.objects.all()
    # personas = Persona.objects.all()
    # contexto = {
    #     'equipos': equipos,
    #     'personas': personas
    # }
    return render(request, 'lista_proyectos.html')
