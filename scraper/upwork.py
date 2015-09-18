import logging
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

from scraper.webdriver import Webdriver

log = logging.getLogger('upwork')


class Upwork(Webdriver):

    def __init__(self):
        super().__init__()

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

    def _to_float(self, string):
        return float(string.replace('.', '').replace(',', '.'))

    def _to_datetime(self, string):
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

    def parse_freelancer(self, url):
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
                hours_worked = self._to_float(el.text.split(' ')[0])
            if 'jobs' in el.text:
                job_count = int(el.text.split(' ')[0])
        freelancer = {
            'url': url,
            'name': name.text,
            'title': title.text,
            'location': location.text,
            'tags': ', '.join([el.text for el in tags]),
            'overview': overview.text,
            'hourly_rate': float(hourly_rate.text[1:].split('/')[0]),
            'rating': float(rating.text),
            'job_success': job_success,
            'hours_worked': hours_worked,
            'job_count': job_count,
            'jobs': self.parse_jobs(),
        }
        log.debug('scraped freelancer {}'.format(freelancer['name']))
        return freelancer

    def parse_jobs(self):
        jobs = []
        work = self.elements(By.CSS_SELECTOR, '.air-card', 'work')[0]
        rows = self.elements(By.CSS_SELECTOR, '.row', 'jobs', parent=work)
        for el in rows:
            name = self.element(By.CSS_SELECTOR, 'a.ng-binding', 'name', el)
            date = self.element(
                By.CSS_SELECTOR, 'p.o-support-info', 'date', el
            )
            start_date, end_date = self._to_datetime(
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
                    hour_count = self._to_float(el.text.split(' ')[0])
                if '/' in el.text:
                    hourly_rate = float(el.text[1:].split(' / ')[0])
                if 'earned' in el.text:
                    earned = self._to_float(el.text[1:].split(' earned')[0])
            job = {
                'name': name.text,
                'start_date': start_date,
                'end_date': end_date,
                'rating': rating,
                'hour_count': hour_count,
                'hourly_rate': hourly_rate,
                'earned': earned,
            }
            log.debug('scraped job {}'.format(job['name']))
            jobs.append(job)
        return jobs

    def scrape_urls(self, url, page_count):
        urls = []
        for i in range(page_count):
            soup = self.soup(url + '&page=' + str(i + 1))
            for el in soup.select('.jsShortName'):
                urls.append('https://www.upwork.com' + el['href'])
        log.debug('scraped {} urls'.format(len(urls)))
        return urls

    def scrape(self, name, email, password, urls):
        try:
            log.debug('starting {} scraper'.format(name))
            self.start()
            self.login(email, password)
            results = []
            for url in urls:
                self.get(url)
                results.append(self.parse_freelancer(url))
            log.debug('stoping {} scraper'.format(name))
            return results
        finally:
            self.stop()


class UpworkInviter(Upwork):

    def send(self, message_str, category_str, title_str, description_str,
             type_str, duration_str, workload_str, public_str):
        contact_button = self.element(By.LINK_TEXT, 'Contact', 'contact')
        self.click(contact_button, 'contact')
        message = self.element(By.ID, 'message', 'message')
        self.clear(message, 'message')
        self.send_keys(message, 'message', message_str)
        category_str, subcategory_str = category_str.split(' | ')
        category = self.element(By.ID, 'category', 'category')
        self.select(category, 'category', category_str)
        subcategory = self.element(By.ID, 'subcategory', 'subcategory')
        self.select(subcategory, 'subcategory', subcategory_str)
        title = self.element(By.ID, 'title', 'title')
        self.send_keys(title, 'title', title_str)
        description = self.element(By.ID, 'description', 'description')
        self.send_keys(description, 'description', description_str)
        if type == 'Fixed price':
            fixed_price = self.element(By.ID, 'job_type-Fixed', 'fixed price')
            self.click(fixed_price, 'fixed price')
        duration = self.element(By.ID, 'job_length', 'duration')
        self.select(duration, 'duration', duration_str)
        workload = self.element(By.ID, 'job_hours', 'workload')
        self.select(workload, 'workload', workload_str)
        if not public_str:
            public = self.element(By.ID, 'visibility', 'public')
            self.click(public, 'public')
        invite = self.element(By.ID, 'submit', 'invite')
        self.click(invite, 'invite')

    def invite(self, name, email, password, message, category, title,
               description, type, duration, workload, public, urls):
        try:
            log.debug('starting {} inviter'.format(name))
            self.start()
            self.login(email, password)
            for url in urls:
                self.get(url)
                self.send(
                    message, category, title, description, type, duration,
                    workload, public
                )
            log.debug('stoping {} inviter'.format(name))
        finally:
            self.stop()
