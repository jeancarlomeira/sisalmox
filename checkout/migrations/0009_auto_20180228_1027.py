# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-28 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0008_cartitem_unity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Aguardando Publicação'), (1, 'Concluida'), (2, 'Cancelada')], default=0, verbose_name='Situação'),
        ),
    ]
