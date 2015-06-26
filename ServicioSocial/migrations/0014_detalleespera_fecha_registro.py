# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0013_auto_20150625_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleespera',
            name='fecha_registro',
            field=models.DateTimeField(default=django.utils.datetime_safe.datetime.now, auto_now=True),
            preserve_default=True,
        ),
    ]
