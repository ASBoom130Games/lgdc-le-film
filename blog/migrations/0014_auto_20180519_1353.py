# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-19 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180519_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_lien',
            field=models.CharField(default='https://pmcvariety.files.wordpress.com/2016/11/warriors-20161120_092416-med-ret.jpg?w=1000&h=563&crop=1', max_length=400),
        ),
    ]