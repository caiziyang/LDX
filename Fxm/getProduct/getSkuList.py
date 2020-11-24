import  requests

from Fxm.data.rwYaml import readYaml


def getSkuList(proIds):
    url = 'https://m.lhs11.com/fxm/services/local/fxm/product/product@query_sku_list.japi'

    params = {'variables[product_id]': proIds}
    re = requests.get(url, params=params)
    return re.json()

def test():
    productIds = readYaml('DataproductID.yaml')
    for productId in productIds:
        r = getSkuList(productId)
        print(r['result']['rows'])
