# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0003_auto_20170814_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontocompany',
            name='EndDate',
            field=models.DateField(default=21, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='persontocompany',
            name='StartDate',
            field=models.DateField(default=21, verbose_name='Start Date'),
        ),
    ]
