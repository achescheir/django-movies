# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-07 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings_app', '0002_auto_20160507_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='video_release_date',
            field=models.DateTimeField(null=True),
        ),
    ]