from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ['nombre', 'autor', 'publicado']

    # Validación de ejemplo: no permitir fechas futuras ojo es importante para validar cualquier cosa seguir la convencion clean_<campo>
    def clean_publicado(self):
        publicado = self.cleaned_data['publicado']
        if publicado > date.today():
            raise ValidationError("La fecha de publicación no puede ser futura.")
        return publicado
    

"""
Esto es lo que manda el front
JSON 

{"nombre": "Pepillo","autor":"Haans","Publicado":"2025-09-22"}

"""