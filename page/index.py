# -*- coding: utf-8 -*-
# Script Name   : index.py
# Author        : Caiziyang
# Created       : 2021/5/8 9:35
# Last Modified : 2021/5/8 9:35
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.login import Login
from page.register import Register
from page.model_page import ModelPage


class Index(BasePage):
    """
    登陆后的页面
    """

    _base_url = 'https://mt.lhs11.com/dzm'

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return Register(self._driver)

    # 跳转登陆页面
    def goto_login(self):
        self._driver.find_element(By.XPATH, '//*[@class="current"]')
        return Login(self._driver)

    # 获取登陆的姓名
    def get_user(self):
        return self._driver.find_element(By.LINK_TEXT, '蔡子扬')

    # 跳转基础型号页面
    def goto_model_page(self):
        self._driver.find_element(By.LINK_TEXT, '产品管理').click()
        self._driver.find_element(By.LINK_TEXT, "基础型号").click()
        return ModelPage(self._driver)

