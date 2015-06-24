# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('iniciales', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('capacidad', models.IntegerField()),
                ('dia', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_termino', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField()),
                ('numero_horas', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_registro_inicio', models.DateField()),
                ('fecha_registro_fin', models.DateField()),
                ('requisitos', models.TextField()),
                ('semestre_maximo', models.IntegerField()),
                ('semestre_minimo', models.IntegerField()),
                ('carreras', models.ManyToManyField(to='ServicioSocial.Carrera')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.TextField()),
                ('descripcion', models.TextField()),
                ('direccion', models.TextField()),
                ('iniciales', models.TextField()),
                ('link_mapa', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='ubicacion',
            field=models.ForeignKey(to='ServicioSocial.Ubicacion'),
            preserve_default=True,
        ),
    ]
