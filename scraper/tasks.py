import logging
import traceback
from datetime import datetime

from celery import shared_task

from scraper.upwork import UpworkScraper
from scraper.models import Freelancer, Job

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
        url = generate_url(
            scraper_obj.category, scraper_obj.experience, scraper_obj.query
        )
        scraper = UpworkScraper(scraper_obj.name)
        urls = scraper.scrape_urls(url, scraper_obj.page_count)
        scraper.login(scraper_obj.account.email, scraper_obj.account.password)
        results = scraper.scrape_freelancers(urls)
        for result in results:
            jobs = result.pop('jobs')
            freelancer, _ = Freelancer.objects.get_or_create(**result)
            for job in jobs:
                Job.objects.get_or_create(freelancer=freelancer, **job)
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
