# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-06 14:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20180228_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_option',
        ),
    ]
