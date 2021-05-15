# -*- coding: utf-8 -*-
# Script Name   : base_page.py
# Author        : Caiziyang
# Created       : 2021/5/8 9:34
# Last Modified : 2021/5/8 9:34
# Version       : 1.0.1
# Modifications : 
#
# Description   :

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import time


class BasePage(object):

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.set_window_size(1495, 1060)
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
        else:
            self._driver = driver

    def close(self):
        time.sleep(20)
        self._driver.quit()