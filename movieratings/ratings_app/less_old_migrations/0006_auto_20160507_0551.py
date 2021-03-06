# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0005_auto_20160507_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdb_url',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video_release_date',
            field=models.DateField(null=True),
        ),
    ]
