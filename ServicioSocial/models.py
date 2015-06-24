from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Ubicacion(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()
    direccion = models.TextField()
    iniciales = models.TextField()
    link_mapa = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre


@python_2_unicode_compatible
class Carrera(models.Model):
    iniciales = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Grupo(models.Model):
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    dia = models.DateField()
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    proyecto = models.ForeignKey('Proyecto', blank=True, null=True)

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Proyecto(models.Model):
    descripcion = models.TextField()
    numero_horas = models.IntegerField()
    nombre = models.CharField(max_length=200)
    fecha_registro_inicio = models.DateField()
    fecha_registro_fin = models.DateField()
    requisitos = models.TextField()
    semestre_maximo = models.IntegerField()
    semestre_minimo = models.IntegerField()
    ubicacion = models.ForeignKey(Ubicacion)
    carreras = models.ManyToManyField(Carrera)
    administrador = models.ForeignKey(User)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre

