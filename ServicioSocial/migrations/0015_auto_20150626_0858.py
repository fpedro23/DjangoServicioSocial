# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0014_detalleespera_fecha_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.CharField(default=b'Lunes', max_length=15,
                                         choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'),
                                                  (b'Miercoles', b'Miercoles'), (b'Jueves', b'Jueves'),
                                                  (b'Viernes', b'Viernes'), (b'Sabado', b'Sabado'),
                                                  (b'Domingo', b'Domingo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='horario',
            name='dia',
        ),
        migrations.AddField(
            model_name='horario',
            name='dias',
            field=models.ManyToManyField(to='ServicioSocial.Dia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='detalleespera',
            name='fecha_registro',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
