# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-22 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180220_1549'),
        ('checkout', '0005_auto_20160930_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='unity',
            field=models.ManyToManyField(to='catalog.Unidades'),
        ),
    ]
