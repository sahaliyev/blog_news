# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='number',
            field=models.IntegerField(),
        ),
    ]
