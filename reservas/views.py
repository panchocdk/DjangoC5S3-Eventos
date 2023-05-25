from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from.models import Empleado, Cliente, Coordinador
from .forms import EmpleadoForm, ClienteForm

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
   

#Vista para Registrar un nuevo Cliente

def crear_cliente(request):
    #Instancia de ClienteForm
    form=ClienteForm()
    if request.POST:
        form=ClienteForm(request.POST)
        if form.is_valid():
            cliente=Cliente(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
            )
            cliente.save()
            return redirect('/listar_clientes/') #listar_clientes falta hacer
        else:
            return redirect('/listar_clientes/')
    context={
        'form':form
        }
    return render(request, 'crear_cliente.html', context)

 #vista activar_coordinador 
def activar_coordinador(request, id):
    try:
        coordinador = Coordinador.objects.get(id=id)
        coordinador.activo = True
        coordinador.save()
        mensaje = "Registro de coordinador activado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'activar_coordinador.html', context)
    except Coordinador.DoesNotExist:
        mensaje = "El coordinador no existe."
        context = {'mensaje': mensaje}
        return render(request, 'activar_coordinador.html', context)
    
#vista desactivar_cliente   
def desactivar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.activo = False
        cliente.save()
        mensaje = "Registro de cliente desactivado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_cliente.html', context)
    except Empleado.DoesNotExist:
        mensaje = "El cliente no existe."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_cliente.html', context)
