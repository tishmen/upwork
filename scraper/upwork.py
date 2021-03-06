import logging
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from scraper.webdriver import Webdriver
from scraper.models import Freelancer, FreelancerJob

log = logging.getLogger('upwork')


class Upwork(Webdriver):

    def login(self, email_str, password_str):
        self.get('https://www.upwork.com/login')
        try:
            email = self.element(By.ID, 'login_username', 'email')
        except WebDriverException:
            email = self.element(By.ID, 'username', 'email')
        self.send_keys(email, 'email', email_str)
        try:
            password = self.element(By.ID, 'login_password', 'password')
        except WebDriverException:
            password = self.element(By.ID, 'password', 'password')
        self.send_keys(password, 'password input', password_str)
        try:
            login = self.element(By.TAG_NAME, 'button', 'login')
        except WebDriverException:
            login = self.element(By.ID, 'submit', 'login')
        self.click(login, 'login')


class UpworkScraper(Upwork):

    def to_float(self, string):
        return float(string.replace('.', '').replace(',', '.'))

    def to_datetime(self, string):
        # Jun 2015 - Present
        # Jun 2015 - Jul 2015
        # Jun 2015
        split = string.split(' - ')
        if len(split) == 2:
            if split[1] == 'Present':
                split[1] = datetime.now().strftime('%b %Y')
            start_date = datetime.strptime(split[0], '%b %Y')
            end_date = datetime.strptime(split[1], '%b %Y')
        else:
            start_date = datetime.strptime(split[0], '%b %Y')
            end_date = None
        return start_date, end_date

    def parse_freelancer(self, url, scraper_id):
        try:
            more_button = self.element(By.LINK_TEXT, 'more', 'more link')
            self.click(more_button, 'more link')
        except WebDriverException:
            pass
        try:
            more_span = self.element(
                By.CSS_SELECTOR, 'o-profile-overview .oTruncateToggleText',
                'more span'
            )
            self.click(more_span, 'more span')
        except WebDriverException:
            pass
        name = self.element(By.CSS_SELECTOR, 'o-name-and-title h1', 'name')
        title = self.element(By.CSS_SELECTOR, 'o-name-and-title h3', 'title')
        location = self.element(
            By.CSS_SELECTOR, 'h3[itemprop="address"]', 'location'
        )
        tags = self.elements(By.CSS_SELECTOR, '.o-tag', 'tags')
        overview = self.element(
            By.CSS_SELECTOR, 'o-profile-overview', 'overview'
        )
        hourly_rate = self.element(
            By.CSS_SELECTOR, 'span[itemprop="pricerange"]', 'hourly rate'
        )
        rating = self.element(
            By.CSS_SELECTOR, 'strong[itemprop="ratingValue"]', 'rating'
        )
        job_success = hours_worked = job_count = None
        for el in self.elements(
                By.CSS_SELECTOR, 'h5.ng-binding', 'work history'):
            if 'Job Success' in el.text:
                job_success = int(el.text.split('%')[0]) / 100
            if 'hours worked' in el.text:
                hours_worked = self.to_float(el.text.split(' ')[0])
            if 'jobs' in el.text:
                job_count = int(el.text.split(' ')[0])
        try:
            freelancer_obj = Freelancer.objects.get(url=url)
        except Freelancer.DoesNotExist:
            freelancer_obj = Freelancer(
                scraper_id=scraper_id,
                url=url,
                name=name.text,
                title=title.text,
                location=location.text,
                tags=', '.join([el.text for el in tags]),
                overview=overview.text,
                hourly_rate=float(hourly_rate.text[1:].split('/')[0]),
                rating=float(rating.text),
                job_success=job_success,
                hours_worked=hours_worked,
                job_count=job_count,
            )
            freelancer_obj.save()
            log.debug('saved freelancer {}'.format(name.text))
        return freelancer_obj

    def parse_jobs(self, freelancer_obj):
        work = self.elements(By.CSS_SELECTOR, '.air-card', 'work')[0]
        rows = self.elements(By.CSS_SELECTOR, '.row', 'jobs', parent=work)
        for el in rows:
            name = self.element(By.CSS_SELECTOR, 'a.ng-binding', 'name', el)
            date = self.element(
                By.CSS_SELECTOR, 'p.o-support-info', 'date', el
            )
            start_date, end_date = self.to_datetime(
                date.get_attribute('innerHTML').strip()
            )
            try:
                rating = self.element(
                    By.CSS_SELECTOR, '.clearfix strong', 'rating', el
                ).text
            except WebDriverException:
                rating = None
            hour_count = hourly_rate = earned = None
            for el in self.elements(
                    By.CSS_SELECTOR, '.text-right div', 'job details',
                    parent=el):
                if 'hour' in el.text:
                    hour_count = self.to_float(el.text.split(' ')[0])
                if '/' in el.text:
                    hourly_rate = float(el.text[1:].split(' / ')[0])
                if 'earned' in el.text:
                    earned = self.to_float(el.text[1:].split(' earned')[0])
            try:
                FreelancerJob.objects.get(
                    freelancer=freelancer_obj, name=name.text
                )
                return
            except FreelancerJob.DoesNotExist:
                freelancer_job_obj = FreelancerJob(
                    freelancer=freelancer_obj,
                    name=name.text,
                    start_date=start_date,
                    end_date=end_date,
                    rating=rating,
                    hour_count=hour_count,
                    hourly_rate=hourly_rate,
                    earned=earned,
                )
                freelancer_job_obj.save()
            log.debug('saved job {}'.format(name.text))

    def scrape_urls(self, url, page_count):
        urls = []
        for i in range(page_count):
            soup = self.soup(url + '&page=' + str(i + 1))
            for el in soup.select('.jsShortName'):
                urls.append('https://www.upwork.com' + el['href'])
        log.debug('scraped {} urls'.format(len(urls)))
        return urls

    def scrape(self, email, password, urls, scraper_id):
        try:
            self.start()
            self.login(email, password)
            for url in urls:
                self.get(url)
                try:
                    freelancer = self.parse_freelancer(url, scraper_id)
                    if freelancer:
                        self.parse_jobs(freelancer)
                except WebDriverException:
                    continue
        except Exception:
            self.onerror()
            raise
        finally:
            self.stop()


class UpworkJob(Upwork):

    def contact(self, message_str, name_str, freelancer):
        contact_button = self.element(By.LINK_TEXT, 'Contact', 'contact')
        self.click(contact_button, 'contact')
        message = self.element(By.ID, 'message', 'message')
        self.clear(message, 'message')
        self.send_keys(message, 'message', message_str)
        opening = self.element(By.ID, 'opening', 'opening')
        self.select(opening, 'opening', name_str)
        invite = self.element(By.ID, 'submit', 'invite')
        self.click(invite, 'invite')
        freelancer.invited = True
        freelancer.save()

    def invite(self, name, email, password, message, freelancers):
        try:
            self.start()
            self.login(email, password)
            for freelancer in freelancers:
                self.get(freelancer.url)
                try:
                    self.contact(message, name, freelancer)
                except WebDriverException:
                    continue
        except Exception:
            self.onerror()
            raise
        finally:
            self.stop()
