# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0010_auto_20150918_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='job_success',
            field=models.FloatField(null=True),
        ),
    ]
