from django.contrib import admin

from ServicioSocial.models import *
from ServicioSocial.forms import *

# Register your models here.


class UsuariosInLine(admin.TabularInline):
    model = DetalleEspera
    form = AddDetalleEsperaForm
    extra = 0


class UsuarioGrupoInLine(admin.TabularInline):
    model = DetalleInscripcion
    extra = 0
    readonly_fields = ['email', ]

    def email(self, instance):
        return instance.usuario.email

    email.short_description = 'Email'


class HorarioInLine(admin.StackedInline):
    model = Horario
    extra = 0


class GrupoInLine(admin.StackedInline):
    model = Grupo
    extra = 1


class ListaEsperaAdmin(admin.ModelAdmin):
    inlines = (UsuariosInLine, )


class GrupoAdmin(admin.ModelAdmin):
    inlines = [HorarioInLine, UsuarioGrupoInLine]


class ProyectoAdmin(admin.ModelAdmin):
    inlines = (GrupoInLine, )
    fieldsets = (
        ('Descripcion de proyecto', {
            'fields': ('nombre', 'administrador', 'descripcion', 'numero_horas', 'ubicacion', 'fecha_inicio_proyecto',
                       'fecha_termino_proyecto')
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
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(ListaEspera, ListaEsperaAdmin)