from django import forms
from .models import Empleado, Cliente

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields ='nombre','apellido','numero_legajo'


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields ='nombre','apellido'