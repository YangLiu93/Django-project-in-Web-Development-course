# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20170422_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return_order',
            name='RTimeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
