# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-26 20:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_cycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='livres',
            name='cycle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Cycle'),
            preserve_default=False,
        ),
    ]
