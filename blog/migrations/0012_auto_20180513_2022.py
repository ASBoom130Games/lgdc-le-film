# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-13 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180424_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='image/affiche-warriors-movie.jpeg', upload_to='image/'),
        ),
    ]
