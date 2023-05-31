from django import forms
from .models import Empleado, Cliente, Coordinador, Servicio

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields ='nombre','apellido','numero_legajo'


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields ='nombre','apellido'

class CoordinadorForm(forms.ModelForm):

    class Meta:
        model = Coordinador
        fields = 'nombre','apellido','numero_documento'

class ServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = 'nombre','descripcion','precio'