# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-07 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180220_1549'),
        ('checkout', '0010_remove_order_payment_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='unity',
            new_name='unid',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='unid',
            field=models.ManyToManyField(to='catalog.Unidades'),
        ),
    ]
