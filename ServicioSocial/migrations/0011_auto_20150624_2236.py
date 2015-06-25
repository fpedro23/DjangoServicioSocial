# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ServicioSocial', '0010_auto_20150624_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='alumnos_inscritos',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='listaespera',
            name='grupo',
            field=models.ForeignKey(default=1, to='ServicioSocial.Grupo', unique=True),
            preserve_default=True,
        ),
    ]
