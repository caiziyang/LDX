import requests
import json
import pytest
import pandas as pd

class PositExport(object):
    """

    """

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    # M端导出数据
    def fxm_posit_export(self, page_number) -> json:
        body_json = {
                "method": "ms_query_log",
                "params": {
                    "pagenumber": page_number,
                    "pagesize": 1000,
                    "variables": {
                        "id": "123456789"
                    }
                }
            }

        posit_export_json = requests.post(url=self.url, headers=self.headers, json=body_json, verify=False).json()
        return posit_export_json

    # 读取Excel文件
    def read_csv(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            for fLine in f:
                print(fLine)

    def read_excel(self, file):
        return pd.read_csv(file, sep=',', index_col=0)


def test_fxm_posit_export():
    url = 'https://mt.lhs11.com/fxm/services/local/fxm/card/cashcard.japi'
    headers = {"cookie": "RSESSIONID=YD9B4LMGLEW2IKHX7ODHZSFAHJ8NJMII"}
    posit_export = PositExport(url, headers)
    for i in range(1, 54):
        posit_export_json = posit_export.fxm_posit_export(i)
        for data in posit_export_json['result']['rows']:
            if data["idtype"] == 1:
                data["idtype"] = '消费者'
            else:
                data["idtype"] = '员工'
            try:
                datas = """{},{},{},{}""".format(data["gmt_create"], data["data"], data["log_userid"], data["idtype"])
            except KeyError:
                datas = """{},{},{},{}""".format(data["gmt_create"], data["data"], "", data["idtype"])

            with open('2.txt', 'a+',  newline='\n', encoding='utf-8') as f:
                f.writelines(datas + '\r\n')













