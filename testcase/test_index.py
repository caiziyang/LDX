# -*- coding: utf-8 -*-
# Script Name   : test_index.py
# Author        : Caiziyang
# Created       : 2021/5/8 9:35
# Last Modified : 2021/5/8 9:35
# Version       : 1.0.1
# Modifications : 
#
# Description   :
from page.index import Index


class TestIndex:

    # 类启动加载，跳转注册页面
    def setup(self):
        self.index = Index()

    # 注册页面输入的元素
    def test_register(self):
        self.index.goto_register()\
            .register("xxx公司")\
            .manager_name("xxx")\
            .corp_industry("IT服务")\
            .corp_scale_btn("1-50人")\
            .register_tel('13128629906')

    def test_login(self):
        self.index.goto_login().scan_qrcode()
        self.user = self.index.get_user().text
        if self.user == "蔡子扬":
            self.index.goto_model_page()\
                .goto_add_page()\
                .spec_name("【深圳.门票】深圳欢乐谷『成人全天票』· 惊喜价220元（价值230元），过山车、跳楼机、大摆锤、4D动感影院、碰碰车...等你来挑战！")\
                .cost_price(213)\
                .advance_day(1)\
                .begin_time('2021-05-15')\
                .end_time('2021-06-24')\
                .order_flow("1")\
                .inventory(100)\
                .singer_name("王嘉文")\
                .time(1)\
                .name_company("1")\
                .settlement_name('广州市阿')\
                .supplier_name('测试电子码')\
                .payment_date()

        # self.register_page = self.index.goto_register().register("xxx集团")
        # assert "请选择" in "|".join(self.register_page.get_error_massage("xx.xx"))

    def teardown(self):
        self.index.close()

