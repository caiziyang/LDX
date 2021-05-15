import requests


class AddOrder(object):

    def __init__(self, url, headers, json):
        self.url = url
        self.headers = headers
        self.json = json

    def post_res(self):
        res = requests.post(url=self.url, json=self.json, headers=self.headers, verify=False)
        return res.json()


def submit_order(product_id, sku_id, room_id, buy_count: int):
    url = """https://fx3t-ysqg.lhs11.com/v1/fxc4-api/pay/submit"""
    headers = {'user-token': '2ui0UkpXTupnWkp0T525Tk7c2Fp@',
               'content-type': 'application/json'}
    json = {
                "buyInfo": "[{\"name\":\"订单联系人\",\"customizeds\":["
                           "{\"num\":1,\"name\":\"姓名\",\"must\":1,"
                           "\"control\":1,\"id\":13773,\"follow_change\":0,"
                           "\"value\":\"蔡子扬\"},{\"is_authentication_tips\":0,"
                           "\"is_idcard_tips\":0,\"num\":1,\"name\":\"手机\","
                           "\"must\":1,\"control\":2,\"id\":13773,\"follow_change\":0,"
                           "\"value\":\"13128629906\"}]}]",
                "cityId": "1",
                "buyCount": buy_count,
                "couponCode": "",
                "customerNote": "",
                "isBuyAxt": 0,
                "productId": product_id,
                "returnUrl": "",
                "skuId": sku_id,
                "payWay": "3.0",
                "platform": "H5",
                "roomId": room_id,
                "shelfId": "138",
                "card": "123456789"
            }
    add_order = AddOrder(url, headers, json)

    return add_order.post_res()


def call_back(fx_order_id, order_id):
    url = 'https://fx3t-ysqg.lhs11.com/v1/fxc4-api/pay/callBack'
    headers = {'user-token': '2uY0UF_12F_n2kP125212FZGUY@@',
               'content-type': 'application/json'}
    params = {'fxOrderId': fx_order_id,
              'orderId': order_id
              }
    res = requests.get(url=url, params=params, headers=headers, verify=False)

    return res.json()


def main(status):
    """
    1 正常发码，数量为1
    2 正常发码 数量为2
    3 发第三方码 数量为1
    4 发第三方码 数量为2
    5 不发码
    6 供应链产品，产品中心有第三方码记录
    """
    if status == 1:
        get_order_ids = submit_order("5272", '8165', '103791', 100)
    elif status == 2:
        get_order_ids = submit_order("5238", '8119', '103718', 1)
    elif status == 3:
        get_order_ids = submit_order("5239", '8120', '103719', 1)
    elif status == 4:
        get_order_ids = submit_order("5239", '8121', '103721', 1)
    elif status == 5:
        get_order_ids = submit_order("5240", '8122', '103720', 1)

    fx_order_id = get_order_ids['result']['payResult']['result']['orderid']
    order_id = get_order_ids['result']['orderId']
    print(call_back(order_id, fx_order_id))


if __name__ == '__main__':
    for _ in range(1):
        main(1)




