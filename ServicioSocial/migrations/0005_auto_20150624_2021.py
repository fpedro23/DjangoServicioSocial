# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServicioSocial', '0004_proyecto_administrador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_termino', models.TimeField()),
                ('grupo', models.ForeignKey(blank=True, to='ServicioSocial.Grupo', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ListaEspera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aprobado', models.NullBooleanField()),
                ('proyecto', models.ForeignKey(to='ServicioSocial.Proyecto')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='listaespera',
            unique_together=set([('usuario', 'proyecto')]),
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='dia',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='hora_inicio',
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='hora_termino',
        ),
    ]
