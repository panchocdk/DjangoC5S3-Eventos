from django.urls import path
from . import views

urlpatterns = [
    path('crear_empleado/', views.crear_empleado, name='crear_empleado'),
    path('actualizar_empleado/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('listar_empleados/', views.listar_empleados, name='listar_empleados')
]