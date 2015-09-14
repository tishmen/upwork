# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=250)),
                ('tags', models.TextField()),
                ('overview', models.TextField()),
                ('hourly_rate', models.FloatField()),
                ('rating', models.FloatField()),
                ('job_success', models.FloatField()),
                ('hours_worked', models.IntegerField()),
                ('job_count', models.IntegerField()),
                ('available', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('hour_count', models.IntegerField(null=True, blank=True)),
                ('hourly_rate', models.IntegerField(null=True, blank=True)),
                ('earned', models.IntegerField(null=True, blank=True)),
                ('freelancer', models.ForeignKey(to='scraper.Freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Scraper',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('page_count', models.IntegerField(default=1)),
                ('account', models.ForeignKey(to='scraper.Account')),
            ],
        ),
    ]
