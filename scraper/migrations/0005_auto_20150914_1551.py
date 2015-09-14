# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0004_auto_20150914_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='hour_count',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
