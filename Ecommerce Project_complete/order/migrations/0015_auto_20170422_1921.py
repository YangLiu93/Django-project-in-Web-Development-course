# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20170422_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='return_order',
            name='ReturnFeedback',
        ),
        migrations.AddField(
            model_name='return_order',
            name='ReturnOption_choices',
            field=models.CharField(choices=[('Cashback', 'Cashback'), ('Replacement', 'Replacement'), ('EKart Credits', 'EKart Credits')], default=1, max_length=500),
            preserve_default=False,
        ),
    ]
