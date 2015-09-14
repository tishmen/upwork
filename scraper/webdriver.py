import logging
import time
import random
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

log = logging.getLogger('upwork')


class Webdriver(object):

    def __init__(self):
        self.min_sleep = 5
        self.max_sleep = 10
        self.stamp = datetime.now().isoformat()

    def start(self):
        self.webdriver = webdriver.Firefox()
        self.webdriver.maximize_window()
        log.debug('started webdriver')

    def stop(self):
        self.webdriver.quit()
        log.debug('stoped webdriver')

    def sleep(self):
        seconds = random.uniform(self.min_sleep, self.max_sleep)
        log.debug('sleeping {} seconds'.format(seconds))
        time.sleep(seconds)

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
