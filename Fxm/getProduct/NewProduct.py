from Fxm.Utility.HttpRequest import HttpRequest
from Fxm.config.rwYaml import readYaml

from Fxm.data.readRequestParameter import getUrl, getHeaders

class NewProduct(object):
    def add_dzm_product(self):
        reads = readYaml("DataproductQuery.yaml")
        for data in reads:
            url = getUrl()[4]['url']
            headers = getHeaders()[1]
            method = getUrl()[4]['method']
            res = HttpRequest.http_request(method, url, data, headers)
        return res

    def add_sku(self, product_id,product_code):
        url = getUrl()[5]['url']
        headers = getHeaders()[1]
        method = getUrl()[5]['method']
        reads = readYaml("DatagetSku.yaml")
        data = reads['productSku'][0][0]
        params = {'variables[sort_num]': data['sort_num'],
        'variables[sku_id]': data['sku_id'],
        'variables[sku_val_id]': data['sku_val_id'],
        'variables[product_id]': product_id,
        'variables[product_code]': product_code
        }
        res = HttpRequest.http_request(method, url, params, headers)
        return res


    def add_skulist(self):
        ...




