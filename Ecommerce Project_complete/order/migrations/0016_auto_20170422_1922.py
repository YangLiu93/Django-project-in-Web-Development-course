# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-22 23:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20170422_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='return_order',
            old_name='ReturnOption_choices',
            new_name='ReturnOptions',
        ),
    ]
