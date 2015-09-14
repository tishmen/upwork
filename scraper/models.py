from django.db import models

from scraper.choices import *


class Account(models.Model):

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


class Scraper(models.Model):

    name = models.CharField(max_length=100, unique=True)
    account = models.ForeignKey('Account')
    page_count = models.IntegerField(default=1)
    query = models.CharField(max_length=100)
    category = models.CharField(
        max_length=250, null=True, blank=True, choices=CATEGORY_CHOICES
    )
    feedback = models.CharField(
        max_length=250, null=True, blank=True, choices=FEEDBACK_CHOICES
    )
    experience = models.CharField(
        max_length=250, null=True, blank=True, choices=EXPERIENCE_CHOICES
    )
    last_run = models.DateTimeField(null=True, blank=True)
    success = models.BooleanField(default=False)
    traceback = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Freelancer(models.Model):

    url = models.URLField(unique=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    tags = models.TextField()
    overview = models.TextField()
    hourly_rate = models.FloatField()
    rating = models.FloatField()
    job_success = models.FloatField()
    hours_worked = models.FloatField()
    job_count = models.IntegerField()

    def __str__(self):
        return self.name


class Job(models.Model):

    freelancer = models.ForeignKey('Freelancer')
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    hour_count = models.FloatField(null=True, blank=True)
    hourly_rate = models.IntegerField(null=True, blank=True)
    earned = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
