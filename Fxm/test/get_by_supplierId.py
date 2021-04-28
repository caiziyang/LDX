# -*- coding: utf-8 -*-
# Script Name   : get_by_supplierId.py
# Author        : Caiziyang
# Created       : 2021/4/26 14:23
# Last Modified : 2021/4/26 14:23
# Version       : 1.0.1
# Modifications : 
#
# Description   :

import requests


class GetBySupplierId(object):
    def __init__(self, url, headers, params):
        self.url = url
        self.headers = headers
        self.params = params

    def post_res(self):
        res = requests.get(url=self.url, params=self.params, headers=self.headers, verify=False)
        return res.json()


def get_By_SupplierId(supplier_id):
    url = """https://fx3t-ysqg.lhs11.com/v1/fxc4-api/product/getBySupplierId"""
    headers = {'user-token': '2ui0UkYbUkinWkvbUkxbT57bT_@@',
               'content-type': 'application/json'}
    params = {
        "supplierId": supplier_id
    }
    add_order = GetBySupplierId(url, headers, params)

    return add_order.post_res()


if __name__ == '__main__':
    list_product_id = []
    get_by_supplierId = get_By_SupplierId(8452)["result"]
    print(len(get_by_supplierId))
    for i in range(len(get_by_supplierId)):
       list_product_id.append(get_by_supplierId[i]["id"])
    print(list_product_id)