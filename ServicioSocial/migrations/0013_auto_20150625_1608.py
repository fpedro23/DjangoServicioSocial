# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServicioSocial', '0012_auto_20150624_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.URLField()),
                ('matricula', models.CharField(max_length=10)),
                ('semestre', models.IntegerField()),
                ('telefono', models.CharField(max_length=15)),
                ('carrera', models.ForeignKey(blank=True, to='ServicioSocial.Carrera', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='detalleespera',
            options={'verbose_name_plural': 'Alumnos en la lista de espera'},
        ),
        migrations.AlterModelOptions(
            name='detalleinscripcion',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
    ]
