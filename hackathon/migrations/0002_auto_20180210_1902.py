# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-10 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recordings',
            options={'ordering': ['timestamp']},
        ),
        migrations.AddField(
            model_name='recordings',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recordings',
            name='type',
            field=models.IntegerField(choices=[(1, 'Enquiry'), (2, 'Complaint')], default=0),
        ),
    ]
