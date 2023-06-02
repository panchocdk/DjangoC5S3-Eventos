from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    #-------------EMPLEADOS--------------------------------------------------------------------------------
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('listar_empleados/', views.listar_empleados, name='listar_empleados'),
    path('activar_empleado/<int:id>/', views.activar_empleado, name='activar_empleado'),
    path('desactivar_empleado/<int:id>/', views.desactivar_empleado, name='desactivar_empleado'),
    #-------------CLIENTES----------------------------------------------------------------------------------
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('actualizar_cliente/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('activar_cliente/<int:cliente_id>/', views.activar_cliente, name='activar_cliente'),
    path('desactivar_cliente/<int:id>/', views.desactivar_cliente, name='desactivar_cliente'),
    #-------------COORDINADORES--------------------------------------------------------------------------------
    path('crear_coordinador/', views.crear_coordinador, name='crear_coordinador'),
    path('actualizar_coordinador/<int:coordinador_id>/', views.actualizar_coordinador, name='actualizar_coordinador'),
    path('listar_coordinadores/', views.listar_coordinadores, name='listar_coordinadores'),
    path('activar_coordinador/<int:id>/', views.activar_coordinador, name='activar_coordinador'),
    path('desactivar_coordinador/<int:coordinador_id>/', views.desactivar_coordinador, name='desactivar_coordinador'),
    #--------------SERVICIOS------------------------------------------------------------------------------------
    path('crear_servicio/', views.crear_servicio, name='crear_servicio'),
    path('actualizar_servicio/<int:servicio_id>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('listar_servicios/', views.listar_servicios, name='listar_servicios'),
    path('activar_servicio/<int:id>/', views.activar_servicio, name='activar_servicio'),
    path('desactivar_servicio/<int:id>/', views.desactivar_servicio, name='desactivar_servicio'),
    #---------------------------------------------------------------------------------------------
    path('registrar_reserva/', views.registrar_reserva, name='registrar_reserva'),
    path('eliminar_reserva/<int:id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('actualizar_reserva/<int:reserva_id>/', views.actualizar_reserva, name='actualizar_reserva'),
    path('listar_reservas/', views.listar_reservas, name='listar_reservas'), 
    #---------------------------------------------------------------------------------------------
]

