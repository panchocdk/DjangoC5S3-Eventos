from django.urls import path
from . import views

urlpatterns = [
    path('api/servicios/<int:id>/', views.ver_servicio, name='ver_servicio'),
    path('api/servicios/', views.servicios, name='servicios'),
]