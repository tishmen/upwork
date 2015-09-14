# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0003_auto_20150914_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='hours_worked',
            field=models.FloatField(),
        ),
    ]
