# -*- coding: utf-8 -*-
# Script Name   : login.py
# Author        : Caiziyang
# Created       : 2021/5/8 9:35
# Last Modified : 2021/5/8 9:35
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.register import Register


# 登陆页面
class Login(BasePage):

    # 扫码登陆
    def scan_qrcode(self):
        self._driver.implicitly_wait(20)
        return self
        # return Index(self._driver)

    # 跳转注册页面
    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return Register(self._driver)

