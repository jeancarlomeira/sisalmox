# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-19 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0018_orderitem_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
    ]