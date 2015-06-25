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

    class Meta:
        verbose_name_plural = 'Ubicaciones'
        verbose_name = 'Ubicacion'


@python_2_unicode_compatible
class Carrera(models.Model):
    iniciales = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Horario(models.Model):
    DAYS_CHOICES = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo', 'Domingo'),
    )
    dia = models.CharField(max_length=15, choices=DAYS_CHOICES, default='Lunes')
    hora_inicio = models.TimeField()
    hora_termino = models.TimeField()
    grupo = models.ForeignKey('Grupo', blank=True, null=True)

    def __str__(self):
        return self.dia + ' - ' + self.hora_inicio.__str__() + ' - ' + self.hora_termino.__str__()


@python_2_unicode_compatible
class Grupo(models.Model):
    nombre = models.CharField(max_length=200)
    capacidad = models.IntegerField()
    proyecto = models.ForeignKey('Proyecto', blank=True, null=True)

    def __str__(self):
        return self.nombre + ' - ' + self.proyecto.nombre


@python_2_unicode_compatible
class Proyecto(models.Model):
    descripcion = models.TextField()
    numero_horas = models.IntegerField()
    nombre = models.CharField(max_length=200)
    fecha_registro_inicio = models.DateTimeField()
    fecha_registro_fin = models.DateTimeField()
    requisitos = models.TextField()
    semestre_maximo = models.IntegerField()
    semestre_minimo = models.IntegerField()
    ubicacion = models.ForeignKey(Ubicacion)
    carreras = models.ManyToManyField(Carrera)
    administrador = models.ForeignKey(User, default=1)
    fecha_inicio_proyecto = models.DateField(blank=True, null=True)
    fecha_termino_proyecto = models.DateField(blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.nombre


@python_2_unicode_compatible
class ListaEspera(models.Model):
    usuarios = models.ManyToManyField(User, through='DetalleEspera')
    grupo = models.ForeignKey(Grupo, default=1)

    class Meta:
        verbose_name_plural = 'Listas de Espera'
        verbose_name = 'Lista de espera'

    def __str__(self):
        return self.grupo.nombre + ' - ' + self.grupo.proyecto.nombre


@python_2_unicode_compatible
class DetalleEspera(models.Model):
    lista_espera = models.ForeignKey(ListaEspera)
    usuario = models.ForeignKey(User)
    aprobado = models.NullBooleanField()

    def __str__(self):
        return self.lista_espera.grupo.__str__()

    class Meta:
        unique_together = ('usuario', 'lista_espera')
