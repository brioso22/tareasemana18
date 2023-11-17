from django.shortcuts import render
from django.shortcuts import render
from .models import *
from .formularios import formulario
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def list_med(request):
    medicos = Medico.objects.all()
    return render(request, 'lismed.html',{"lismed":medicos})

def add_med(request):
    if request.method == "POST":
        formularios1 = formulario.Add_medic(request.POST)
        if formulario.is_valid():
            nuevoreg = Medico()
            nuevoreg.nombre = formularios1.data["nombre"]
            nuevoreg.apellido = formularios1.data["apellido"]
            nuevoreg.especialidad = formularios1.data["especialidad"]
            nuevoreg.save()
            return HttpResponseRedirect("/")
    else:
        formularios1 = formulario.Add_medic()
        return render(request,"Add_medic.html",{"form":formularios1})