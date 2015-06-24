from django.conf.urls import patterns, include, url
from django.contrib import admin
from ServicioSocial import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'DjangoServicioSocial.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^registro/', CreateView.as_view(
                           template_name='register.html',
                           form_class=UserCreationForm,
                           success_url='home/',
                       )
                           ),
                       url(r'^lista-proyectos/', views.ProyectosListView.as_view()),
                       url(r'^proyecto/(?P<pk>[-\w]+)/$', views.ProyectoDetailView.as_view()),

                       url(r'^home/', views.home),

                       )
