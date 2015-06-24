from django.contrib import admin

from ServicioSocial.forms import *


# Register your models here.


class GrupoInLine(admin.StackedInline):
    model = Grupo
    form = GrupoAddForm
    extra = 1


class ProyectoAdmin(admin.ModelAdmin):
    inlines = (GrupoInLine, )
    fieldsets = (
        ('Descripcion de proyecto', {
            'fields': ('nombre', 'administrador', 'descripcion', 'numero_horas', 'ubicacion', )
        }),
        ('Fechas de registro', {
            'fields': ('fecha_registro_inicio', 'fecha_registro_fin',)
        }),
        ('Perfil', {
            'fields': ('requisitos', 'semestre_maximo', 'semestre_minimo', 'carreras')
        }),
    )


admin.site.register(Ubicacion)
admin.site.register(Carrera)
admin.site.register(Proyecto, ProyectoAdmin)
