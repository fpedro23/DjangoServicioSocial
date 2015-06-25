from django import forms
from ServicioSocial.models import DetalleEspera, Grupo, DetalleInscripcion


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
            print detalle.usuario
            nuevo_detalle = DetalleInscripcion()
            nuevo_detalle.usuario = detalle.usuario
            nuevo_detalle.aprobado = True
            nuevo_detalle.grupo = instance.lista_espera.grupo
            nuevo_detalle.save()
            detalle.delete()

        return super(AddDetalleEsperaForm, self).save(commit=commit)