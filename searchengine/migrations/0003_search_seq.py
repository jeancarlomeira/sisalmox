# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-12 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchengine', '0002_auto_20180312_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='seq',
            field=models.CharField(default='1', max_length=1, verbose_name='Seq.'),
        ),
    ]
