# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 00:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20171025_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employment',
            old_name='title_name',
            new_name='title',
        ),
    ]