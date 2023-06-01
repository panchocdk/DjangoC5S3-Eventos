from django.shortcuts import render
from reservas.models import Servicio
from django.http import JsonResponse

# Create your views here.

def ver_servicio(request, id):
    try:
        servicio = Servicio.objects.get(id=id)
        data = {
            'id': servicio.id,
            'nombre': servicio.nombre,
            'descripcion': servicio.descripcion,
            'precio': servicio.precio,
        }
    except Servicio.DoesNotExist:
        data = {}  
    return JsonResponse(data, json_dumps_params={'indent': 4}, safe=False)