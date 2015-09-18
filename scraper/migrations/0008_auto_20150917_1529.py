# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0007_auto_20150917_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inviter',
            name='duration',
            field=models.CharField(max_length=100, choices=[('More than 6 months', 'More than 6 months'), ('3 to 6 months', '3 to 6 months'), ('1 to 3 months', '1 to 3 months'), ('Less than 1 month', 'Less than 1 month'), ('Less than 1 week', 'Less than 1 week')]),
        ),
        migrations.AlterField(
            model_name='inviter',
            name='type',
            field=models.CharField(default='Hourly', max_length=100, choices=[('Hourly', 'Hourly'), ('Fixed price', 'Fixed price')]),
        ),
        migrations.AlterField(
            model_name='inviter',
            name='workload',
            field=models.CharField(max_length=100, choices=[('More than 30 hrs/week', 'More than 30 hrs/week'), ('Less than 30 hrs/week', 'Less than 30 hrs/week'), ("I don't know yet", "I don't know yet")]),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='experience',
            field=models.CharField(blank=True, max_length=250, null=True, choices=[('Entry', 'Entry'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')]),
        ),
    ]
