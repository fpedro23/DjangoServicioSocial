# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ServicioSocial', '0006_auto_20150624_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listaespera',
            options={'verbose_name': 'Lista de espera', 'verbose_name_plural': 'Listas de Espera'},
        ),
        migrations.AddField(
            model_name='listaespera',
            name='grupo',
            field=models.ForeignKey(default=1, to='ServicioSocial.Grupo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(default=b'LU', max_length=2,
                                   choices=[(b'LU', b'Lunes'), (b'MA', b'Martes'), (b'MI', b'Miercoles'),
                                            (b'JU', b'Jueves'), (b'VI', b'Viernes'), (b'SA', b'Sabado'),
                                            (b'DO', b'Domingo')]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='listaespera',
            unique_together=set([('usuario', 'grupo')]),
        ),
        migrations.RemoveField(
            model_name='listaespera',
            name='proyecto',
        ),
    ]
