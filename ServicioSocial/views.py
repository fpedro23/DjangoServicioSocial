from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from ServicioSocial.models import *
from django.utils import timezone


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