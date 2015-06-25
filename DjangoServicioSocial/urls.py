from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ServicioSocial import views


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DjangoServicioSocial.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registro/', views.register),
                       url(r'^proyecto/(?P<pk>[-\w]+)/$', views.ProyectoDetailView.as_view()),
                       url(r'^proyecto/inscribir-usuario', views.registrar_espera),
                       url(r'^accounts/login/$', auth_views.login),
                       url(r'^$', views.ProyectosListView.as_view()),
                       url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
                       )
