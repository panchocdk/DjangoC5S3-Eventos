from django.shortcuts import render, redirect
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
            return redirect('/listar_empleados/')
        else:
            return redirect('/listar_empleados/')
    context={
        'form':form
        }
    return render(request, 'crear_empleado.html', context)

#Vista para Actualizar un Empleado
def actualizar_empleado(request, empleado_id):
    try:
        empleado = Empleado.objects.get(id=empleado_id)
        if request.method == 'POST':
            form = EmpleadoForm(request.POST, instance=empleado)
            if form.is_valid():
                form.save()
            return redirect('/listar_empleados/')
        else:
            form = EmpleadoForm(instance=empleado)
        context = {'form': form}
        return render(request, 'actualizar_empleado.html', context)
    except Exception:
        return render(request, 'error.html')
    
#Vista para Listar a los Empleados
def listar_empleados(request):
    try:
        empleados=Empleado.objects.all()
        context={
            'empleados':empleados
        }
        return render(request,'listar_empleados.html', context)
    except Exception:
        return render(request, 'error.html')

#vista activar_empleado 
def activar_empleado(request, id):
    try:
        empleado = Empleado.objects.get(id=id)
        empleado.activo = True
        empleado.save()
        mensaje = "Registro de empleado activado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'activar_empleado.html', context)
    except Empleado.DoesNotExist:
        mensaje = "El empleado no existe."
        context = {'mensaje': mensaje}
        return render(request, 'activar_empleado.html', context)

#vista desactivar_empleado    
def desactivar_empleado(request, id):
    try:
        empleado = Empleado.objects.get(id=id)
        empleado.activo = False
        empleado.save()
        mensaje = "Registro de empleado desactivado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_empleado.html', context)
    except Empleado.DoesNotExist:
        mensaje = "El empleado no existe."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_empleado.html', context)
