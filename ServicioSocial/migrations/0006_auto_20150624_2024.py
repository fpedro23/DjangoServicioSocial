# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0005_auto_20150624_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='fecha_termino',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_registro_fin',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_registro_inicio',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
