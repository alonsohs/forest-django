from django import forms
from .models import Equipo, Persona


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo

        fields = [
            'nombre',
        ]

        labels = {
            'nombre': 'Nombre del equipo',
        }


        widget = {
            'nombre': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona

        fields = [
            'urlImagen',
            'nombre',
            'apellidos',
            'correo',
            'telefono',
            'direccion',
            'rol',
            'equipo'
        ]

        labels = {
            'urlImagen': 'URL de imagen de perfil',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Dirección',
            'rol': 'Rol en el proyecto',
            'equipo': 'Equipo',
        }


        widget = {
            'urlImagen': forms.URLInput(),
            'nombre': forms.TextInput(),
            'apellidos': forms.TextInput(),
            'correo': forms.EmailInput(),
            'telefono': forms.TextInput(),
            'direccion': forms.TextInput(),
            'rol': forms.ChoiceField(),
            'equipo': forms.ChoiceField
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
