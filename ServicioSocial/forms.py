from django import forms

from ServicioSocial.models import *
from django.contrib.auth.models import User


class GrupoAddForm(forms.ModelForm):
    class Meta:
        model = Grupo


