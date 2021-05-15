# -*- coding: utf-8 -*-
# Script Name   : dzm_product_spec_add.py
# Author        : Caiziyang
# Created       : 2021/5/15 15:16
# Last Modified : 2021/5/15 15:16
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from page.base_page import BasePage


class DzmProductSpecAdd(BasePage):

    # 输入型号名称
    def spec_name(self, spec_name):
        self._driver.find_element(By.ID, "name1").send_keys(spec_name)
        return self

    # 输入提前天数
    def advance_day(self, advance_day):
        self._driver.find_element(By.ID, "advanceDay").send_keys(advance_day)
        return self

    # 输入成本价
    def cost_price(self, cost_price):
        self._driver.find_element(By.ID, "costPrice").send_keys(cost_price)
        return self

    def begin_time(self, begin_time):
        self._driver.find_element(By.ID, "begin_time").send_keys(begin_time)
        self._driver.find_element(By.ID, "addorupdate-title").click()
        return self

    def end_time(self, end_time):
        self._driver.find_element(By.ID, "end_time").send_keys(end_time)
        self._driver.find_element(By.ID, "addorupdate-title").click()
        return self

    # 预约流程
    def order_flow(self, value):
        Select(self._driver.find_element(By.NAME, "orderFlow")).select_by_value(value)
        return self

    # 每日库存
    def inventory(self, inventory):
        self._driver.find_element(By.ID, "inventory").send_keys(inventory)
        return self

    # 签约人
    def singer_name(self, singer_name):
        # 先输入搜索的值
        self._driver.find_element(By.ID, "singerName").send_keys(singer_name)
        # 然后定位ul
        ul = self._driver.find_element_by_css_selector("#productSpecForm > div:nth-child(7) > div > ul")
        # 最后定位里面所有值
        li = ul.find_elements_by_tag_name('li')
        # 选取想要的值
        li[0].click()  # 0代表选择第一个值
        return self

    def name_company(self, company_value):
        Select(self._driver.find_element(By.NAME, "nameCompany")).select_by_value(company_value)
        return self

    def sale_company(self):
        Select(self._driver.find_element(By.NAME, "sale_company")).select_by_value("1")
        return self

    def settlement_name(self, settlement_name):
        # 先输入搜索的值
        self._driver.find_element(By.ID, "settlementName").send_keys(settlement_name)
        # 然后定位ul
        ul = self._driver.find_element_by_css_selector("#productSpecForm > div:nth-child(11) > div > ul")
        # 最后定位里面所有值
        li = ul.find_elements_by_tag_name('li')
        # 选取想要的值
        li[0].click()  # 0代表选择第一个值
        return self

    def supplier_name(self, supplier_name):
        # 先输入搜索的值
        self._driver.find_element(By.ID, "supplierName").send_keys(supplier_name)
        # 然后定位ul
        ul = self._driver.find_element_by_css_selector("#productSpecForm > div:nth-child(12) > div > ul")
        # 最后定位里面所有值
        li = ul.find_elements_by_tag_name('li')
        # 选取想要的值
        li[0].click()  # 0代表选择第一个值
        return self

    def payment_date(self):
        self._driver.find_element(By.XPATH, '//*[@id="settleType0"]/div[1]/input[1]').click()
        time.sleep(2)
        self._driver.find_element(By.ID, "m_save").click()
        return self

    def time(self, seconds):
        time.sleep(seconds)
        return self








