# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-19 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180513_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_lien',
            field=models.CharField(default='http://www.croiseedesclans.fr/medias/images/affiche-warriors-movie.jpeg', max_length=400),
        ),
    ]