# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-08 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderId', models.CharField(max_length=250)),
                ('TimeStamp', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdId', models.CharField(max_length=100)),
                ('PName', models.CharField(max_length=100)),
                ('PType', models.CharField(max_length=250)),
                ('PCat', models.CharField(max_length=100)),
                ('PPrice', models.CharField(max_length=250)),
                ('PQuantity', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdOrderId', models.CharField(max_length=250)),
                ('ReturnStatus', models.CharField(max_length=100)),
                ('OrderQuantity', models.CharField(max_length=500)),
                ('CurrentQuantity', models.CharField(max_length=500)),
                ('TotalPrice', models.CharField(max_length=500)),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Orders')),
                ('ProdId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Product')),
            ],
        ),
    ]
