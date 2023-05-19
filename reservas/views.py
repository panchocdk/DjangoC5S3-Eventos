from django.shortcuts import render
from django.http import HttpResponseRedirect
from.models import Empleado
from .forms import EmpleadoForm

# Create your views here.

#Vista para Registrar nuevo Empleados
def crear_empleado(request):
    #Instancia de ProductoForm
    form=EmpleadoForm()
    if request.POST:
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            empleado=Empleado(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                numero_legajo=form.cleaned_data['numero_legajo']
            )
            empleado.save()
        else:
            return HttpResponseRedirect('/crear_empleado/')
    context={
        'form':form
        }
    return render(request, 'crear_empleado.jinja', context)

#Vista para Actualizar un Empleado
def actualizar_empleado(request, empleado_id):
    empleado=Empleado.objects.get(id=empleado_id)
    context={'empleado':empleado}
    if request.POST:
        empleado.nombre=request.POST['nombre']
        empleado.apellido=int(request.POST['apellido'])
        empleado.numero_legajo=request.POST['numero_legajo']
        empleado.save()
    return render(request, 'actualizar_empleado.jinja', context)
    
#Vista para Listar a los Empleados
def listar_empleados(request):
    empleados=Empleado.objects.all()
    context={
        'empleados':empleados
    }
    return render(request,'listar_empleados.html', context)