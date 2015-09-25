import os
import logging
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from django.conf import settings

log = logging.getLogger('upwork')


class Webdriver(object):

    def start(self):
        self.webdriver = webdriver.PhantomJS()
        self.webdriver.maximize_window()
        log.debug('started webdriver')

    def stop(self):
        self.webdriver.quit()
        log.debug('stoped webdriver')

    def sleep(self):
        time.sleep(1)

    def get(self, url):
        self.webdriver.get(url)
        log.debug('got {}'.format(url))
        self.sleep()

    def soup(self, url):
        response = requests.get(url)
        log.debug('got {}'.format(url))
        return BeautifulSoup(response.content, 'html.parser')

    def send_keys(self, element, name, keys):
        element.send_keys(keys)
        log.debug('sent {} to {}'.format(keys, name))
        self.sleep()

    def click(self, element, name):
        element.click()
        log.debug('clicked {}'.format(name))
        self.sleep()

    def select(self, element, name, text):
        options = Select(element)
        options.select_by_visible_text(text)
        log.debug('selected {} for {}'.format(text, name))
        self.sleep()

    def clear(self, element, name):
        element.clear()
        log.debug('cleared {}'.format(name))
        self.sleep()

    def element(self, by, selector, name, parent=None):
        if parent:
            element = parent.find_element(by, selector)
        else:
            element = self.webdriver.find_element(by, selector)
        log.debug('found {} element'.format(name))
        return element

    def elements(self, by, selector, name, parent=None):
        if parent:
            elements = parent.find_elements(by, selector)
        else:
            elements = self.webdriver.find_elements(by, selector)
        log.debug('found {} {} elements'.format(len(elements), name))
        return elements

    def onerror(self):
        stamp = datetime.now().isoformat()
        screenshoot_path = os.path.join(
            settings.ERROR_DIR, '{}.png'.format(stamp)
        )
        self.webdriver.get_screenshot_as_file(screenshoot_path)
        log.debug('took screenshot as {}'.format(screenshoot_path))
        source_path = os.path.join(settings.ERROR_DIR, '{}.html'.format(stamp))
        with open(source_path, 'w') as f:
            f.write(self.webdriver.page_source)
        log.debug('saved source as {}'.format(source_path))
