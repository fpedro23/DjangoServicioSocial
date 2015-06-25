# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0009_auto_20150624_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ubicacion',
            options={'verbose_name': 'Ubicacion', 'verbose_name_plural': 'Ubicaciones'},
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(default=b'Lunes', max_length=15,
                                   choices=[(b'Lunes', b'Lunes'), (b'Martes', b'Martes'), (b'Miercoles', b'Miercoles'),
                                            (b'Jueves', b'Jueves'), (b'Viernes', b'Viernes'), (b'Sabado', b'Sabado'),
                                            (b'Domingo', b'Domingo')]),
            preserve_default=True,
        ),
    ]
