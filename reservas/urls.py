from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('listar_empleados/', views.listar_empleados, name='listar_empleados'),
    path('activar_empleado/<int:id>/', views.activar_empleado, name='activar_empleado'),
    path('desactivar_empleado/<int:id>/', views.desactivar_empleado, name='desactivar_empleado'),
    path('crear_cliente/', views.crear_cliente, name='crear_cliente'),
    path('desactivar_cliente/<int:id>/', views.desactivar_cliente, name='desactivar_cliente'),
    path('activar_coordinador/<int:id>/', views.activar_coordinador, name='activar_coordinador'),
    path('desactivar_coordinador/<int:coordinador_id>/', views.desactivar_coordinador, name='desactivar_coordinador'),
    path('crear_coordinador/', views.crear_coordinador, name='crear_coordinador'),
    path('listar_coordinadores/', views.listar_coordinadores, name='listar_coordinadores'),
    path('actualizar_cliente/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('modificar_empleados/<int:id>/', views.modificar_coordinador, name='modificar_coordinador'),
    path('activar_cliente/<int:cliente_id>/', views.activar_cliente, name='activar_cliente'),
    path('listar_clientes/', views.listar_clientes, name='listar_clientes'),
    path('actualizar_coordinador/<int:coordinador_id>/', views.actualizar_coordinador, name='actualizar_coordinador'),
]