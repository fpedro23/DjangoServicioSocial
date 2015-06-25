# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServicioSocial', '0008_auto_20150624_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleEspera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aprobado', models.NullBooleanField()),
                ('lista_espera', models.ForeignKey(to='ServicioSocial.ListaEspera')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='detalleespera',
            unique_together=set([('usuario', 'lista_espera')]),
        ),
        migrations.AddField(
            model_name='listaespera',
            name='usuarios',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='ServicioSocial.DetalleEspera'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='listaespera',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='listaespera',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='listaespera',
            name='aprobado',
        ),
    ]
