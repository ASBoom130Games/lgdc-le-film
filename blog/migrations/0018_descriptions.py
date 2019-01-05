# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2019-01-05 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_post_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('_corp_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('corp', precise_bbcode.fields.BBCodeTextField(no_rendered_field=True, verbose_name='texte')),
            ],
        ),
    ]