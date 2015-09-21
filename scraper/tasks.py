import logging
import traceback
from datetime import datetime

from celery import shared_task

from scraper.upwork import UpworkScraper, UpworkInviter
from scraper.models import Freelancer, Job
from scraper.map import generate_url

log = logging.getLogger('upwork')


@shared_task(bind=True)
def scrape_task(self, scraper_obj):
    try:
        url = generate_url(
            scraper_obj.category, scraper_obj.experience, scraper_obj.query
        )
        scraper = UpworkScraper()
        urls = scraper.scrape_urls(url, scraper_obj.page_count)
        results = scraper.scrape(
            scraper_obj.name, scraper_obj.account.email,
            scraper_obj.account.password, urls
        )
        for result in results:
            jobs = result.pop('jobs')
            try:
                freelancer_obj = Freelancer.objects.get(url=result['url'])
            except Freelancer.DoesNotExist:
                freelancer_obj = Freelancer(scraper=scraper_obj, **result)
                freelancer_obj.save()
            for job in jobs:
                try:
                    job_obj = Job.objects.get(
                        freelancer=freelancer_obj, name=job['name']
                    )
                except Job.DoesNotExist:
                    job_obj = Job(freelancer=freelancer_obj, **job)
                    job_obj.save()
        scraper_obj.last_run = datetime.now()
        scraper_obj.success = True
        scraper_obj.traceback = None
        scraper_obj.save()
    except Exception as e:
        log.error('Traceback: {}'.format(traceback.format_exc()))
        scraper_obj.success = False
        scraper_obj.traceback = e
        scraper_obj.save()
        raise


@shared_task(bind=True)
def invite_task(self, freelancers, inviter_obj):
    try:
        inviter = UpworkInviter()
        inviter.invite(
            inviter_obj.name, inviter_obj.account.email,
            inviter_obj.account.password, inviter_obj.message,
            inviter_obj.category, inviter_obj.title, inviter_obj.description,
            inviter_obj.type, inviter_obj.duration, inviter_obj.workload,
            inviter_obj.public, [freelancer.url for freelancer in freelancers]
        )
        inviter_obj.last_run = datetime.now()
        inviter_obj.success = True
        inviter_obj.traceback = None
        inviter_obj.save()
    except Exception as e:
        log.error('Traceback: {}'.format(traceback.format_exc()))
        inviter_obj.success = False
        inviter_obj.traceback = e
        inviter_obj.save()
        raise
