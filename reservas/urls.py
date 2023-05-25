from django.urls import path
from . import views

urlpatterns = [
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('listar_empleados/', views.listar_empleados, name='listar_empleados'),
    path('activar_empleado/<int:id>/', views.activar_empleado, name='activar_empleado'),
    path('desactivar_empleado/<int:id>/', views.desactivar_empleado, name='desactivar_empleado'),
    path('activar_coordinador/<int:id>/', views.activar_coordinador, name='activar_coordinador'),
]