# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20171025_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.DateField(blank=True),
        ),
    ]