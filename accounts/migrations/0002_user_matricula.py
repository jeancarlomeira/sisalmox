# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-15 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='matricula',
            field=models.CharField(default='', max_length=6, verbose_name='Matrícula'),
            preserve_default=False,
        ),
    ]