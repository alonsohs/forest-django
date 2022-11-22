from django import forms
from .models import Equipo, Personas


# class EquipoForm(forms.ModelForm):
#     class Meta:
#         model = Equipo
#
#         fields = [
#             'nombre',
#         ]
#
#         labels = {
#             'nombre': 'Nombre del equipo',
#         }
#
#         ALTURA_CHOICES = [
#             ('1', 'Pequeño'),
#             ('2', 'Mediano'),
#             ('3', 'Grande'),
#             ('4', 'Muy grande'),
#         ]
#
#         widget = {
#             'urlImagen': forms.URLInput(),
#             'nombre': forms.TextInput(),
#             'ecosistema': forms.TextInput(),
#             'nombreCientifico': forms.TextInput(),
#             'precio': forms.FloatField(),
#             'altura': forms.ChoiceField(choices=ALTURA_CHOICES),
#             'descripcion': forms.TextInput(),
#             'metrosCuadrados': forms.FloatField()
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({'class': 'form-control'})

