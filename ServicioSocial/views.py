# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from ServicioSocial.forms import UserCreateForm
from ServicioSocial.models import *


def home(request):
    return render(request, "home.html", )


class ProyectosListView(ListView):
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        context['listaespera'] = timezone.now()
        return context


class ProyectoDetailView(DetailView):
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['listaespera'] = timezone.now()
        return context


@login_required
def registrar_espera(request):
    if request.POST.get('id_grupo', None) is None:
        html = "<html><body>Debes de seleccionar al menos un horario para inscribirte</body></html>"

    else:

        try:
            lista_espera = ListaEspera.objects.get(grupo__id=request.POST.get('id_grupo', None))
        except Exception as e:
            lista_espera = ListaEspera()
            print request.POST.get('id_grupo')
            lista_espera.grupo = Grupo.objects.get(id=request.POST.get('id_grupo'))
            lista_espera.save()

        if lista_espera.usuarios.count() >= lista_espera.grupo.capacidad * 2:
            html = "<html><body>Error, La lista de espera esta llena, intenta inscribirte en otro grupo </body></html>"

        else:
            nuevo_detalle = DetalleEspera()
            nuevo_detalle.usuario = request.user
            nuevo_detalle.aprobado = None
            nuevo_detalle.lista_espera = lista_espera

            try:
                nuevo_detalle.save()
                html = "<html><body>Has sido inscrito satisfactoriamente en la lista de espera, espera " \
                       "la autorización del administrador: %s.</body></html>" % lista_espera.grupo
            except Exception as e:
                html = "<html><body>Error, ya te haz inscrito previamente en la lista de espera: %s.</body></html>" % lista_espera.grupo

    return HttpResponse(html)


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            html = "<html>" \
                   "<body>Tu registro se ha creado satisfactoriamente, ahora puedes iniciar sesion" \
                   "<a href=\'/\'> Inicio </a>" \
                   "</body>" \
                   "</html>"
            return HttpResponse(html)
    else:
        form = UserCreateForm
    return render(request, "registration/register.html", {
        'form': form,
    })