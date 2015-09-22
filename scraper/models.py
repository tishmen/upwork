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
        max_length=250, null=True, blank=True,
        choices=CATEGORY_CHOICES + SUBCATEGORY_CHOICES, default='Any Category'
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

    scraper = models.ForeignKey('Scraper')
    url = models.URLField(unique=True)
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    location = models.CharField(max_length=250)
    tags = models.TextField()
    overview = models.TextField()
    hourly_rate = models.FloatField()
    rating = models.FloatField()
    job_success = models.FloatField(null=True, blank=True)
    hours_worked = models.FloatField()
    job_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):

    class Meta:
        unique_together = ('freelancer', 'name')

    freelancer = models.ForeignKey('Freelancer')
    name = models.CharField(max_length=250)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    hour_count = models.FloatField(null=True, blank=True)
    hourly_rate = models.IntegerField(null=True, blank=True)
    earned = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Inviter(models.Model):

    name = models.CharField(max_length=100, unique=True)
    account = models.ForeignKey('Account')
    message = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=250, choices=SUBCATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default='Hourly'
    )
    duration = models.CharField(max_length=100, choices=DURATION_CHOICES)
    workload = models.CharField(max_length=100, choices=WORKLOAD_CHOICES)
    public = models.BooleanField(default=True)
    active = models.BooleanField(default=False)
    last_run = models.DateTimeField(null=True, blank=True)
    success = models.BooleanField(default=False)
    traceback = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
