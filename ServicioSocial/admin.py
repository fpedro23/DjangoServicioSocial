from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ServicioSocial.models import *
from ServicioSocial.forms import *



# Register your models here.


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UsuariosInLine(admin.TabularInline):
    model = DetalleEspera
    form = AddDetalleEsperaForm
    extra = 0

    readonly_fields = ['email', 'first_name', 'last_name', 'carrera', 'telefono', 'facebook', 'matricula', 'semestre',
                       'fecha_registro']

    def email(self, instance):
        return instance.usuario.email

    def first_name(self, instance):
        return instance.usuario.first_name

    def last_name(self, instance):
        return instance.usuario.last_name

    def carrera(self, instance):
        return instance.usuario.userprofile.carrera.iniciales

    def telefono(self, instance):
        return instance.usuario.userprofile.telefono

    def facebook(self, instance):
        return instance.usuario.userprofile.facebook

    def matricula(self, instance):
        return instance.usuario.userprofile.matricula

    def semestre(self, instance):
        return instance.usuario.userprofile.semestre


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'first_name', 'last_name', 'email', )

    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


class UsuarioGrupoInLine(admin.TabularInline):
    model = DetalleInscripcion
    extra = 0
    readonly_fields = ['email', 'first_name', 'last_name', 'carrera', 'telefono', 'facebook', 'matricula', 'semestre']

    def email(self, instance):
        return instance.usuario.email

    def first_name(self, instance):
        return instance.usuario.first_name

    def last_name(self, instance):
        return instance.usuario.last_name

    def carrera(self, instance):
        return instance.usuario.userprofile.carrera.iniciales

    def telefono(self, instance):
        return instance.usuario.userprofile.telefono

    def facebook(self, instance):
        return instance.usuario.userprofile.facebook

    def matricula(self, instance):
        return instance.usuario.userprofile.matricula

    def semestre(self, instance):
        return instance.usuario.userprofile.semestre





    email.short_description = 'Email'
    carrera.short_description = 'Carrera'


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
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)