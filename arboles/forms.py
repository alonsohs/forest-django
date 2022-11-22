from django import forms
from .models import Arbol


class ArbolForm(forms.ModelForm):
    class Meta:
        model = Arbol

        fields = [
            'urlImagen',
            'nombre',
            'ecosistema',
            'nombreCientifico',
            'precio',
            'altura',
            'descripcion',
            'metrosCuadrados'
        ]

        labels = {
            'urlImagen': 'URL de imagen',
            'nombre': 'Nombre del árbol',
            'ecosistema': 'Ecosistema',
            'nombreCientifico': 'Nombre cientifico del árbol',
            'precio': 'Precio aproximado',
            'altura': 'Altura',
            'descripcion': 'Descripción',
            'metrosCuadrados': 'Metros cuadrados de espacio requeridos',
        }

        ALTURA_CHOICES = [
            ('1', 'Pequeño'),
            ('2', 'Mediano'),
            ('3', 'Grande'),
            ('4', 'Muy grande'),
        ]

        widget = {
            'urlImagen': forms.URLInput(),
            'nombre': forms.TextInput(),
            'ecosistema': forms.TextInput(),
            'nombreCientifico': forms.TextInput(),
            'precio': forms.FloatField(),
            'altura': forms.ChoiceField(choices=ALTURA_CHOICES),
            'descripcion': forms.TextInput(),
            'metrosCuadrados': forms.FloatField()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

