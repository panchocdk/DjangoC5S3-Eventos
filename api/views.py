from django.shortcuts import render
from reservas.models import Servicio, Cliente, Empleado, Coordinador
from django.http import JsonResponse

# Create your views here.

def ver_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
        data = {
            'servicio':[{
            'id': servicio.id,
            'nombre': servicio.nombre,
            'descripcion': servicio.descripcion,
            'precio': servicio.precio,
            }]
        }
    except Servicio.DoesNotExist:
        data = {
            'servicio':[]
        }  
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)

def servicios(request): 
    servicios=Servicio.objects.all()
    lista=[]
    for servicio in servicios:
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

def clientes(request): 
    clientes=Cliente.objects.all()
    lista=[]
    for cliente in clientes:
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

def empleados(request): 
    empleados=Empleado.objects.all()
    lista=[]
    for empleado in empleados:
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

def coordinadores(request): 
    coordinadores=Coordinador.objects.all()
    lista=[]
    for coordinador in coordinadores:
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