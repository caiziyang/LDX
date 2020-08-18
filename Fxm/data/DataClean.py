import json

class DataClean(object):

    def data_json(self, productRequstesLists, resjson: json) ->json:
        productList = []
        respon = resjson['result']['rows']

        for i, products in enumerate(respon):
            productInformationList = []
            newProductRequstesLists = []

            for productRequstesList in productRequstesLists:
                products = resjson['result']['rows'][i]
                try:
                    product = products[productRequstesList]
                except KeyError:
                    continue
                productInformationList.append(product)

                if productRequstesList == 'class':
                    newProductRequstesLists.append('variables[' + 'product_' + productRequstesList + ']')
                else:
                    newProductRequstesLists.append('variables[' + productRequstesList + ']')

            product2 = dict(zip(newProductRequstesLists, productInformationList))

            productList.append(product2)

        return productList

