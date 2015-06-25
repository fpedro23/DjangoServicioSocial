from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from ServicioSocial.models import *


def home(request):
    return render(request, "home.html", )


class ProyectosListView(ListView):
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectosListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ProyectoDetailView(DetailView):
    model = Proyecto

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@login_required
def registrar_espera(request):
    print 'Well done'
    print request.user.id
    print request.POST.get('id_grupo', None)
    return HttpResponse('Hi')