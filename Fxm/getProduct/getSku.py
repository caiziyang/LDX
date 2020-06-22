import  requests


def getSku(proIds):
    list = []
    url = 'https://m.lhs11.com/fxm/services/local/fxm/product/product@query_sku.japi'

    for proId in proIds:
        params = {'variables[product_id]': proId}
        re = requests.get(url, params=params)
        list.append(re.json())
    return list

