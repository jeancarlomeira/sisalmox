# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180308_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='unid',
        ),
    ]