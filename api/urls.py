from django.urls import path
from . import views

urlpatterns = [
    path('ver_servicio/<int:id>/', views.ver_servicio, name='ver_servicio'),
]