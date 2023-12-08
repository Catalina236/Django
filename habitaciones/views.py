from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hab
from .forms import HabForm
from rest_framework import viewsets
from .serializer import HabitacionSerializer
# Create your views here.
def inicio(request):
    habitaciones=Hab.objects.all()
    print(habitaciones)
    return render(request,"home.html",{'habitaciones':habitaciones})
def ir_hab(request):
    return render(request,'habitacion.html')
def crear(request):
    formulario=HabForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request,'registrar.html',{'formulario':formulario})

def editar(request, codigo):
    hab=Hab.objects.get(codigo=codigo)
    formulario=HabForm(request.POST or None, request.FILES or None, instance=hab)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('inicio')
    return render(request, 'editar.html',{'formulario':formulario})
        
def eliminar(request, codigo):
    hab=Hab.objects.get(codigo=codigo)
    hab.delete()
    return redirect('inicio')
class HabitacionViewSet(viewsets.ModelViewSet):
    queryset=Hab.objects.all()
    serializer_class=HabitacionSerializer