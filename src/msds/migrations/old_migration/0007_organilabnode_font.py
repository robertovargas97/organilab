# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-09 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msds', '0006_auto_20180709_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='organilabnode',
            name='font',
            field=models.CharField(default='12px arial white', max_length=25),
        ),
    ]