# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_auto_20150914_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='earned',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
