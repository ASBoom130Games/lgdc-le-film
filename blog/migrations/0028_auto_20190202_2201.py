# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-02-02 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_auto_20190202_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livres',
            name='date_en',
            field=models.CharField(default=1, max_length=200, verbose_name='date de parution anglaise'),
            preserve_default=False,
        ),
    ]