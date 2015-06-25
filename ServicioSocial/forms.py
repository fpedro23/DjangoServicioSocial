from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from ServicioSocial.models import DetalleEspera, DetalleInscripcion, UserProfile, Carrera


class AddDetalleEsperaForm(forms.ModelForm):
    class Meta:
        model = DetalleEspera
        fields = '__all__'

    def save(self, commit=True):
        instance = super(AddDetalleEsperaForm, self).save(commit=True)
        print instance.lista_espera.detalleespera_set.filter(aprobado=True)
        print instance.lista_espera.grupo
        DetalleInscripcion.objects.filter(grupo__id=instance.lista_espera.grupo.id).delete()

        for detalle in instance.lista_espera.detalleespera_set.filter(aprobado=True):
            nuevo_detalle = DetalleInscripcion()
            nuevo_detalle.usuario = detalle.usuario
            nuevo_detalle.aprobado = True
            nuevo_detalle.grupo = instance.lista_espera.grupo
            nuevo_detalle.save()

        return super(AddDetalleEsperaForm, self).save(commit=commit)


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    facebook = forms.URLField(required=True)
    matricula = forms.CharField(max_length=10)
    semestre = forms.IntegerField()
    telefono = forms.CharField(max_length=15)
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "email", "username", "password1", "password2",)

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=True)
        user.email = self.cleaned_data["email"]

        user_profile = UserProfile()
        user_profile.user = user
        user_profile.facebook = self.cleaned_data['facebook']
        user_profile.matricula = self.cleaned_data['matricula']
        user_profile.semestre = self.cleaned_data['semestre']
        user_profile.telefono = self.cleaned_data['telefono']
        user_profile.carrera = self.cleaned_data['carrera']

        if commit:
            user.save()
            user_profile.user.id = user.id
            user_profile.save()
        return user