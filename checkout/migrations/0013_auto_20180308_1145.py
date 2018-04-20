# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_product_unid'),
        ('checkout', '0012_auto_20180308_1120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='unid',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='unid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='catalog.Unidades', verbose_name='Unidades'),
            preserve_default=False,
        ),
    ]
