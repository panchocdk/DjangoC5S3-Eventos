from django.shortcuts import render
from reservas.models import Servicio, Cliente, Empleado, Coordinador
from django.http import JsonResponse

# Create your views here.
#Vista endpoint para ver un registro de servicio
def ver_servicio(request, id):
    try:
        #Accede al registro de servicio cuyo id corresponda con el ingresado
        servicio = Servicio.objects.get(id=id)
        #Los datos que se muestran son: id, nombre, descripcion y precio
        data = {
            'servicio':[{
            'id': servicio.id,
            'nombre': servicio.nombre,
            'descripcion': servicio.descripcion,
            'precio': servicio.precio,
            }]
        }
    except Servicio.DoesNotExist:
        #Si no se encuentra un registro con el id enviado, muestra una lista vacía
        data = {
            'servicio':[]
        }  
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)

#Vista endpoint para ver el listado de servicio
def servicios(request): 
    #Accede a todos los servicios registrados
    servicios=Servicio.objects.all()
    lista=[]
    for servicio in servicios:
        #Los datos que se muestran por cada servicio son: id, nombre y precio
        firstdata ={
            'id': (servicio.id),
            'nombre': (servicio.nombre),
            'precio': (servicio.precio),
            }
        lista.append(firstdata)
    data = {
        'servicios': lista
        }
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)

#Vista endpoint para ver el listado de clientes
def clientes(request): 
    #Accede a todos los clientes registrados
    clientes=Cliente.objects.all()
    lista=[]
    for cliente in clientes:
        #Los datos que se muestran por cada cliente son: id, nombre, apellido y estado
        firstdata ={
            'id': (cliente.id),
            'nombre': (cliente.nombre),
            'apellido': (cliente.apellido),
            'activo' : (cliente.activo),
            }
        lista.append(firstdata)
    data = {
        'clientes': lista
        }
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)

#Vista endpoint para ver el listado de empleados
def empleados(request): 
    #Accede a todos los empleados registrados
    empleados=Empleado.objects.all()
    lista=[]
    for empleado in empleados:

        #Los datos que se muestran por empleado son: id, nombre, apellido, numero de legajo y estado
        firstdata ={
            'id': (empleado.id),
            'nombre': (empleado.nombre),
            'apellido': (empleado.apellido),
            'numero_legajo': (empleado.numero_legajo),
            'activo' : (empleado.activo),
            }
        lista.append(firstdata)
    data = {
        'empleados': lista
        }
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)

#Vista endpoint para ver el listado de coordinadores
def coordinadores(request): 
    #Accede a todos los coordinadores registrados
    coordinadores=Coordinador.objects.all()
    lista=[]
    for coordinador in coordinadores:
        #Los datos que se muestran por coordinador son: id, nombre, apellido, nro de documento,fecha de alta y estado
        firstdata ={
            'id': (coordinador.id),
            'nombre': (coordinador.nombre),
            'apellido': (coordinador.apellido),
            'numero_documento': (coordinador.numero_documento),
            'fecha_alta': (coordinador.fecha_alta),
            'activo' : (coordinador.activo),
            }
        lista.append(firstdata)
    data = {
        'coordinadores': lista
        }
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)