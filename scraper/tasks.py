import logging
import traceback
from datetime import datetime

from celery import shared_task

from scraper.upwork import UpworkScraper, UpworkJob

log = logging.getLogger('upwork')


def generate_url(category, experience, query):
    url = 'https://www.upwork.com/o/profiles/browse/'
    if category:
        split = category.split(', ')
        url += 'c/{}/'.format(split[0])
        if len(split) == 2:
            url += 'sc/{}/'.format(split[1])
    url += '?q='.format(query)
    if experience:
        url += '&ex='.format(experience)
    return url


@shared_task(bind=True)
def scrape_task(self, scraper_obj):
    try:
        log.debug('starting scrape task for {} '.format(scraper_obj.name))
        url = generate_url(
            scraper_obj.category, scraper_obj.experience, scraper_obj.query
        )
        scraper = UpworkScraper()
        urls = scraper.scrape_urls(url, scraper_obj.page_count)
        scraper.scrape(
            scraper_obj.account.email, scraper_obj.account.password, urls,
            scraper_obj.id
        )
        scraper_obj.last_run = datetime.now()
        scraper_obj.success = True
        scraper_obj.traceback = None
        scraper_obj.save()
        log.debug('stoping scrape task for {} '.format(scraper_obj.name))
    except Exception as e:
        log.error('Traceback: {}'.format(traceback.format_exc()))
        scraper_obj.success = False
        scraper_obj.traceback = e
        scraper_obj.save()
        raise


@shared_task(bind=True)
def invite_task(self, freelancers, job_obj):
    try:
        log.debug('starting invite task for {} '.format(job_obj.name))
        job = UpworkJob()
        job.invite(
            job_obj.name, job_obj.account.email, job_obj.account.password,
            job_obj.message, freelancers
        )
        job_obj.last_run = datetime.now()
        job_obj.success = True
        job_obj.traceback = None
        job_obj.save()
        log.debug('stoping invite task for {} '.format(job_obj.name))
    except Exception as e:
        log.error('Traceback: {}'.format(traceback.format_exc()))
        job_obj.success = False
        job_obj.traceback = e
        job_obj.save()
        raise
