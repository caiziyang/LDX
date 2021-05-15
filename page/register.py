# -*- coding: utf-8 -*-
# Script Name   : register.py
# Author        : Caiziyang
# Created       : 2021/5/8 9:35
# Last Modified : 2021/5/8 9:35
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from selenium.webdriver.common.by import By
from page.base_page import BasePage


class Register(BasePage):

    def register(self, corp_name):
        self._driver.find_element(By.ID, "corp_name").send_keys(corp_name)
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def manager_name(self, manager_name):
        self._driver.find_element(By.ID, "manager_name").send_keys(manager_name)
        self._driver.find_element(By.ID, "submit_btn").click()
        return self

    def corp_industry(self, corp_industry):
        self._driver.find_element(By.XPATH, '//*[@id="corp_industry"]/a').click()
        self._driver.find_element(By.LINK_TEXT, corp_industry).click()
        self._driver.find_element(By.LINK_TEXT, "计算机软件/硬件/信息服务").click()
        return self

    def corp_scale_btn(self, corp_scale_btn):
        self._driver.find_element(By.XPATH, '//*[@id="corp_scale_btn"]/a').click()
        self._driver.find_element(By.LINK_TEXT, corp_scale_btn).click()
        return self

    def register_tel(self, register_tel):
        self._driver.find_element(By.ID, "register_tel").send_keys(register_tel)
        self._driver.find_element(By.ID, "get_vcode").click()

    def get_error_massage(self):
        result = []
        for element in self._driver.find_elementS(By.CSS_SELECTOR, ".js_error_msg"):
            result.append(element.text)
        return result



