from django.shortcuts import render
from reservas.models import Servicio
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