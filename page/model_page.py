# -*- coding: utf-8 -*-
# Script Name   : model_page.py
# Author        : Caiziyang
# Created       : 2021/5/15 14:43
# Last Modified : 2021/5/15 14:43
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from selenium.webdriver.common.by import By
from page.base_page import BasePage
from page.dzm_product_spec_add import DzmProductSpecAdd


class ModelPage(BasePage):

    def goto_add_page(self):
        self._driver.implicitly_wait(3)
        self._driver.switch_to.frame("iframe5")
        self._driver.find_element(By.LINK_TEXT, '新增').click()
        return DzmProductSpecAdd(self._driver)

    def delete_spec(self):
        pass