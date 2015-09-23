import logging
import time
import random

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select

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
        seconds = random.uniform(5, 10)
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
