# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-20 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180131_1041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unid',
        ),
        migrations.AddField(
            model_name='product',
            name='unid',
            field=models.ManyToManyField(to='catalog.Unidades'),
        ),
    ]