from django import forms

from ServicioSocial.models import *


class GrupoAddForm(forms.ModelForm):
    class Meta:
        model = Grupo