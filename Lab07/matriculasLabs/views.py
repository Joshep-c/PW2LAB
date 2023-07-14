from django.shortcuts import render
from .models import Asignatura

def tabla_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'lista.html', {'asignaturas': asignaturas})