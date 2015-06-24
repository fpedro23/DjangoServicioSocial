# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0002_proyecto_grupos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='grupos',
        ),
        migrations.AddField(
            model_name='grupo',
            name='proyecto',
            field=models.ForeignKey(blank=True, to='ServicioSocial.Proyecto', null=True),
            preserve_default=True,
        ),
    ]
