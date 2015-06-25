# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServicioSocial', '0011_auto_20150624_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleInscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aprobado', models.NullBooleanField()),
                ('grupo', models.ForeignKey(to='ServicioSocial.Grupo')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='detalleinscripcion',
            unique_together=set([('usuario', 'grupo')]),
        ),
        migrations.RemoveField(
            model_name='grupo',
            name='alumnos_inscritos',
        ),
        migrations.AddField(
            model_name='grupo',
            name='alumnos',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='ServicioSocial.DetalleInscripcion'),
            preserve_default=True,
        ),
    ]
