from django.urls import path
from . import views

urlpatterns = [
    path('api/servicios/<int:id>/', views.ver_servicio, name='ver_servicio'),
    path('api/servicios/', views.servicios, name='servicios'),
    path('api/clientes/', views.clientes, name='clientes'),
    path('api/empleados/', views.empleados, name='empleados'),
    path('api/coordinadores/', views.coordinadores, name='coordinadores'),
]