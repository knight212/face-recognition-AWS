# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-12 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0006_athlete_profile_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='image',
            field=models.ImageField(default=None, upload_to=b'', verbose_name=b'Athletes/Images'),
            preserve_default=False,
        ),
    ]
