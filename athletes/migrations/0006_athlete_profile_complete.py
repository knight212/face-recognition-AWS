# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-12 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0005_athlete_is_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='profile_complete',
            field=models.BooleanField(default=False),
        ),
    ]
