# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-21 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytenders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tender',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tender',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_number',
            field=models.TextField(),
        ),
    ]