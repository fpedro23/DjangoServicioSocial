from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views

from ServicioSocial import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DjangoServicioSocial.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registro/', CreateView.as_view(
                           template_name='registration/register.html',
                           form_class=UserCreationForm,
                           success_url='home/',
                       )
                           ),
                       url(r'^proyecto/(?P<pk>[-\w]+)/$', views.ProyectoDetailView.as_view()),
                       url(r'^proyecto/inscribir-usuario', views.registrar_espera),
                       url(r'^accounts/login/$', auth_views.login),
                       url(r'^$', views.ProyectosListView.as_view()),

                       )
