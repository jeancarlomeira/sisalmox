# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-23 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_cartitem_unity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='unity',
        ),
    ]
