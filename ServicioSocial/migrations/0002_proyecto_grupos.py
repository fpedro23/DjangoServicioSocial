# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='grupos',
            field=models.ManyToManyField(to='ServicioSocial.Grupo'),
            preserve_default=True,
        ),
    ]
