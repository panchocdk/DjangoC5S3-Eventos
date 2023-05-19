from django.contrib import admin
from . import models

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['nombre','apellido','numero_legajo','activo']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['nombre', 'apellido']

    #list filter: muestra un filtro para todos los objetos
    list_filter=['activo']

class CoordinadorAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['nombre','apellido','numero_documento','fecha_alta','activo']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['nombre', 'apellido']

    #list filter: muestra un filtro para todos los objetos
    list_filter=['activo']

class ClienteAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['nombre','apellido','activo']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['nombre', 'apellido']

    #list filter: muestra un filtro para todos los objetos
    list_filter=['activo']

class ServicioAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['nombre','descripcion','precio','activo']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['nombre']

    #list filter: muestra un filtro para todos los objetos
    list_filter=['activo']

class ReservaDeServicioAdmin(admin.ModelAdmin):
    #list display: muestra los atributos del objeto en forma de lista
    list_display=['fecha_creacion','fecha_reserva','cliente','responsable','empleado','servicio','precio']

    #search fields: abre un campo 'Search' para poder buscar por los campos indicados
    search_fields=['responsable','cliente','empleado','servicio']


#Registro de modelos en ADMIN
admin.site.register(models.Empleado, EmpleadoAdmin)
admin.site.register(models.Coordinador, CoordinadorAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Servicio, ServicioAdmin)
admin.site.register(models.ReservaDeServicio, ReservaDeServicioAdmin)
