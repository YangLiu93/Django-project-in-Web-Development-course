# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20170422_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return_order',
            name='ReturnId',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
