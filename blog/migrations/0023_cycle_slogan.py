# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-27 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_cycle_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycle',
            name='slogan',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
