from django.shortcuts import render, redirect
from.models import Empleado, Cliente, Coordinador, Servicio, ReservaDeServicio
from .forms import EmpleadoForm, ClienteForm, CoordinadorForm, ServicioForm, ReservaDeServicioForm
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

def inicio(request):
    return render(request, 'index.html')


#-----------------------EMPLEADOS-----------------------------------------------------------------
 

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


#-------------------------CLIENTES-----------------------------------------------------------------------------------


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
            cliente.save() #Se guardan los datos ingresados 
            return redirect('/listar_clientes/') #Redirecciona al listado de clientes 
        else:
            return redirect('/listar_clientes/')
    context={
        'form':form
        }
    return render(request, 'crear_cliente.html', context)

#Vista para Actualizar un Cliente
def actualizar_cliente(request, cliente_id):
    try:
        #Busca el cliente al que le corresponde la id ingresada
        cliente = Cliente.objects.get(id=cliente_id)
        if request.method == 'POST':
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save() #Se guardan los datos actualizados
            return redirect('/listar_clientes/') #Redirecciona al listado de clientes
        else:
            form = ClienteForm(instance=cliente)
        context = {'form': form}
        return render(request, 'actualizar_cliente.html', context)
    except Exception:
        return render(request, 'error.html') 

#Vista para Listar a los Clientes     
def listar_clientes(request):
    try:
        #Accede a todos los clientes registrados
        clientes = Cliente.objects.all()
        context = {
            'clientes': clientes
        }
        return render(request, 'listar_clientes.html', context)
    except Exception:
        return render(request, 'error.html')

#vista activar cliente
def activar_cliente(request, cliente_id):
    try:
        #Accede al cliente que corresponde con la id ingresada
        cliente = Cliente.objects.get(id=cliente_id)
        cliente.activo = True
        cliente.save() #Guarda el nuevo estado del cliente
        mensaje = "Registro de cliente activado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'activar_cliente.html', context)
    except Cliente.DoesNotExist:
        mensaje = "El cliente no existe."
        context = {'mensaje': mensaje}
        return render(request, 'activar_cliente.html', context)

#vista desactivar_cliente   
def desactivar_cliente(request, id):
    try:
        #Accede al cliente que corresponde con la id ingresada
        cliente = Cliente.objects.get(id=id)
        cliente.activo = False
        cliente.save() #Guarda el nuevo estado del cliente
        mensaje = "Registro de cliente desactivado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_cliente.html', context)
    except Cliente.DoesNotExist:
        mensaje = "El cliente no existe."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_cliente.html', context)


#-----------------------COORDINADORES----------------------------------------------------------------------------


#Vista para Registrar nuevos Coordinadores
def crear_coordinador(request):
    form = CoordinadorForm()
    if request.method == 'POST':
        form = CoordinadorForm(request.POST)
        if form.is_valid():
            numero_documento = form.cleaned_data['numero_documento']
            if Coordinador.objects.filter(numero_documento=numero_documento).exists():
                messages.error(request, 'El número de documento ya está en uso.')
            else:
                coordinador = form.save(commit=False)
                coordinador.save()
                messages.success(request, 'El coordinador se creó correctamente.')
                return redirect('/listar_coordinadores/')
        else:
            # Pasar los mensajes de error al formulario
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{form.fields[field_name].label}: {error}')

    context = {'form': form}
    return render(request, 'crear_coordinador.html', context)

#Vista para actualizar un Coordinador
def actualizar_coordinador(request, coordinador_id):
    try:
        coordinador = Coordinador.objects.get(id=coordinador_id)
        if request.method == 'POST':
            form = CoordinadorForm(request.POST, instance=coordinador)
            if form.is_valid():
                form.save()
                return redirect('/listar_coordinadores/')
        else:
            form = CoordinadorForm(instance=coordinador)
        context = {'form': form}
        return render(request, 'actualizar_coordinador.html', context)
    except Exception:
        return render(request, 'error.html')
    
#Vista para Listar a los Coordinadores
def listar_coordinadores(request):
    try:
        coordinadores=Coordinador.objects.all()
        context={
            'coordinadores':coordinadores
        }
        return render(request,'listar_coordinadores.html', context)
    except Exception:
        return render(request, 'error.html')

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

#Vista para Desactivar un Coordinador   
def desactivar_coordinador(request, coordinador_id):
    try:
        coordinador = Coordinador.objects.get(id=coordinador_id)
        coordinador.activo = False
        coordinador.save()
        mensaje = "Registro de coordinador desactivado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_coordinador.html', context)
    except Coordinador.DoesNotExist:
        mensaje = "El coordinador no existe."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_coordinador.html', context)
    

#------------------SERVICIOS----------------------------------------------------------------------------------


#vista para registrar servicios 
def crear_servicio(request):
    #Instancia de ServicioForm
    form=ServicioForm()
    if request.POST:
        form=ServicioForm(request.POST)
        if form.is_valid():
            servicio=Servicio(
                nombre=form.cleaned_data['nombre'],
                descripcion=form.cleaned_data['descripcion'],
                precio=form.cleaned_data['precio'],    
            )
            servicio.save()
            return redirect('/listar_servicios/')
        else:
            return redirect('/listar_servicios/')
    context={
        'form':form
        }
    return render(request, 'crear_servicio.html', context)

#Vista para actualizar un Servicio
def actualizar_servicio(request, servicio_id):
    try:
        servicio = Servicio.objects.get(id=servicio_id)
        if request.method == 'POST':
            form = ServicioForm(request.POST, instance=servicio)
            if form.is_valid():
                form.save()
                return redirect('/listar_servicios/')
        else:
            form = ServicioForm(instance=servicio)
        context = {'form': form}
        return render(request, 'actualizar_servicio.html', context)
    except Exception:
        return render(request, 'error.html')
    
#view para el listado de servicios
def listar_servicios(request):
    try:
        servicios=Servicio.objects.all()
        context={
            'servicios':servicios
        }
        return render(request,'listar_servicios.html', context)
    except Exception:
        return render(request, 'error.html')
    
#Vista para activar un servicio
def activar_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = True
        servicio.save()
        mensaje = "Registro de servicio activado correctamente."
        context = {'mensaje':mensaje}
        return render(request, 'activar_servicio.html', context)
    except Servicio.DoesNotExist:
        mensaje = "El servicio no existe."
        context = {'mensaje': mensaje}
        return render(request, 'activar_servicio.html', context)
    
#view para desactivar servicios
def desactivar_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
        servicio.activo = False
        servicio.save()
        mensaje = "Registro de servicio desactivado correctamente."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_servicio.html', context)
    except Servicio.DoesNotExist:
        mensaje = "El servicio no existe."
        context = {'mensaje': mensaje}
        return render(request, 'desactivar_servicio.html', context)
    

#----------------RESERVA DE SERVICIOS-------------------------------------------------------------


#vista para registrar reservas de servicio
def crear_reserva(request):
    #Instancia de ServicioForm
    form=ReservaDeServicioForm()
    if request.POST:
        form=ReservaDeServicioForm(request.POST)
        if form.is_valid():
            reserva=ReservaDeServicio(
                fecha_reserva=form.cleaned_data['fecha_reserva'],
                cliente=form.cleaned_data['cliente'],
                responsable=form.cleaned_data['responsable'],
                empleado=form.cleaned_data['empleado'],
                servicio=form.cleaned_data['servicio'],
            )
            reserva.save()            
            return redirect('/listar_reservas/')
        else:
            return redirect('/listar_reservas/')
    context={
        'form':form
        }
    return render(request, 'crear_reserva.html', context)

#Vista para actualizar una Reserva de Servicio
def actualizar_reserva(request, reserva_id):
    try:
        reserva = ReservaDeServicio.objects.get(id=reserva_id)
        if request.method == 'POST':
            form = ReservaDeServicioForm(request.POST, instance=reserva)
            if form.is_valid():
                form.save()
                return redirect('/listar_reservas/')
        else:
            form = ReservaDeServicioForm(instance=reserva)
        context = {'form': form}
        return render(request, 'actualizar_reserva.html', context)
    except Exception:
        return render(request, 'error.html')

#Vista para el listado de Reservas de Servicios
def listar_reservas(request):
    try:
        reservas=ReservaDeServicio.objects.all()
        context={
            'reservas':reservas
        }
        return render(request,'listar_reservas.html', context)
    except Exception:
        return render(request, 'error.html')
    
#Vista para eliminar una reserva de servicio 
def eliminar_reserva(request, id):
    try:
        reserva = ReservaDeServicio.objects.get(id=id)    
        if request.POST:
            reserva.delete()
            return redirect('/eliminar_ok/')
        context={'reserva':reserva}
        return render(request, 'eliminar_reserva.html', context)
    except Exception:
        return render(request, 'error.html')
    
#Vista para confirmar eliminacion
def eliminar_ok(request):
    return render(request, 'eliminar_ok.html')