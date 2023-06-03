from django import forms
from .models import Empleado, Cliente, Coordinador, Servicio, ReservaDeServicio

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

class ReservaDeServicioForm(forms.ModelForm):

    class Meta:
        model = ReservaDeServicio
        fields = 'fecha_reserva', 'cliente', 'responsable', 'empleado', 'servicio'
        widgets = {
            'fecha_reserva': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ModelChoiceField) and (field_name=='cliente' or field_name=='responsable' or field_name=='empleado' or field_name=='servicio'):
                field.queryset = field.queryset.filter(activo=True)