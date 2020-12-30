import json

import requests


class GetProductQuery(object):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    # 获取货架信息接口

    def query_city_shelf(self):

        url = self.url
        headers = self.headers
        query_json = {
                    "order": "asc",
                    "limit": 1000,
                    "offset": 0,
                    "method": "query",
                    "params": {
                        "pagenumber": 1,
                        "pagesize": 1000,
                        "variables": {
                            "shelf_id": "",
                            "id": "",
                            "name": "",
                            "block": "",
                            "shelf_type": ""
                        }
                    }
                }

        shelf_ids_json = requests.post(url=url, headers=headers, json=query_json).json()
        return shelf_ids_json

    def query_simple_shelf(self, shelf_id):
        url = self.url
        headers = self.headers
        query_simple_shelf_json = {
                "method": "query_simple_shelf",
                "params": {
                    "variables": {
                        "id": shelf_id
                        }
                    }
                }

        city_ids_json = requests.post(url=url, headers=headers, json=query_simple_shelf_json).json()
        return city_ids_json

    def save_Shelf_City_Sort(self, shelf_id, collate_id):
        url = self.url
        headers = self.headers
        save_shelf_city_sort_json = {
                "method": "saveShelfCitySort",
                "params": {
                    "variables": {
                        "id": shelf_id,
                        "block": "",
                        "city_collation": [{
                            "city_id": "23",
                            "sorder": collate_id
                            },
                            {
                            "city_id": "1",
                            "sorder": collate_id
                                }
                            ]
                        }
                    }
                }

        city_ids_json = requests.post(url=url, headers=headers, json=save_shelf_city_sort_json).json()
        return city_ids_json


def main():
    url = 'https://mt.lhs11.com/fxm/services/local/fxm/city/city_shelf.japi'
    headers = {'cookie': 'RSESSIONID=163JCHQ323ZRWBIDF4L6BOQQH0XZMQVN'}
    product_query = GetProductQuery(url=url, headers=headers)
    shelf_ids_json = product_query.query_city_shelf()

    for index, shelf_dis in enumerate(shelf_ids_json['result']['rows']):
        shelf_id = shelf_dis['id']
        city_ids_json = product_query.query_simple_shelf(shelf_id)
        city_lists = city_ids_json['result']['city_collation'][0]
        # 返回数据为空，返回的是empty
        if city_lists != 'e':
            # 判断城市的id 是否为南宁
            if city_lists['city_id'] == 23:
                sorder = city_lists['sorder']

                product_query.save_Shelf_City_Sort(shelf_id, sorder)


if __name__ == '__main__':
    main()
