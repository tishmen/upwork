# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20150914_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='scraper',
            name='last_run',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scraper',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scraper',
            name='traceback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
