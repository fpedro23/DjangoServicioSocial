# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0007_auto_20150624_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='fecha_termino',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fecha_inicio_proyecto',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='fecha_termino_proyecto',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
