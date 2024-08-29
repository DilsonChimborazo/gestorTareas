from django.shortcuts import render, redirect
from .models import Tarea
from .form import TareaForm

# Create your views here.

def crear(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    form = TareaForm()
    return render(request,'crear.html',{'form':form})

def listar(request):
    tareas = Tarea.objects.all()
    return render(request,'listar.html',{'tareas':tareas})

def tarea_Completa(request):
    tareas = Tarea.objects.filter(completed=True)  # Filtra solo las tareas completadas
    return render(request, 'tareas.html', {'tareas': tareas})

def tarea_Incompleta(request):
    tareas = Tarea.objects.filter(completed=False)  # Filtra solo las tareas incompletas
    return render(request, 'tareas.html', {'tareas': tareas})