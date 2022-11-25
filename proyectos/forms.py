from django import forms
from .models import Proyecto


class DateInput(forms.DateInput):
    input_type = 'date'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto

        fields = [
            'nombre',
            'urlImagen',
            'fecha_inicio',
            'fecha_limite',
            'presupuesto',
            'presupuesto_arboles',
            'ubicacion',
            'lider',
            'status',
            'tipo_suelo',
            'metros_cuadrados',
            'clima',
            'tipo_arbol',
            'latitud',
            'longitud',
            'equipo',
        ]

        labels = {
            'nombre': 'Nombre del proyecto',
            'urlImagen': 'URL Imagen del proyecto',
            'fecha_inicio': 'Fecha de inicio',
            'fecha_limite': 'Fecha de terminación',
            'presupuesto': 'Presupuesto incial',
            'presupuesto_arboles': 'Cantidad de arboles disponibles (opcional)',
            'ubicacion': 'Dirección de la zona',
            'lider': 'Lider del proyecto',
            'status': 'Estatus del proyecto',
            'tipo_suelo': 'Tipo de suelo en la zona',
            'metros_cuadrados': 'Metros cuadrados disponibles',
            'clima': 'Tipo de clima',
            'tipo_arbol': 'Tipo de árbol a plantar',
            'latitud': 'Coordenada Latitud',
            'longitud': 'Coordenada Longitud',
            'equipo': 'Equipo asignado',
        }

        widget = {
            'urlImagen': forms.URLInput(),
            'nombre': forms.TextInput(),
            'fecha_inicio': forms.SelectDateWidget(),
            'fecha_limite': forms.DateInput(attrs={'class': 'datepicker', 'id': 'data_input'}),
            'presupuesto': forms.FloatField(),
            'presupuesto_arboles': forms.FloatField(),
            'ubicacion': forms.TextInput(),
            'lider': forms.ChoiceField(),
            'status': forms.ChoiceField(),
            'tipo_suelo': forms.ChoiceField(),
            'metros_cuadrados': forms.FloatField(),
            'clima': forms.ChoiceField(),
            'tipo_arbol': forms.ChoiceField(),
            'latitud': forms.FloatField(),
            'longitud': forms.FloatField(),
            'equipo': forms.ChoiceField(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
