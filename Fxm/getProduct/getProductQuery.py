from Fxm.Utility.HttpRequest import HttpRequest


class getProductQuery(object):

    # 获取产品信息请求
    def productQuery(self, pagesize: int, method, url, headers, productRequstesLists):

        productList = []
        params = {"pagenumber": 1, "pagesize": pagesize, "variables[product_class]": "dzm"}

        re = HttpRequest.http_request(method, url, params, headers)


        # 数据清理

        for i in range(pagesize):
            productInformationList = []

            newProductRequstesLists = []

            for productRequstesList in productRequstesLists:
                products = re['result']['rows'][i]
                try:
                    product = products[productRequstesList]
                except KeyError:
                    continue
                productInformationList.append(product)

                if productRequstesList == 'class':
                    newProductRequstesLists.append('variables[' + 'product_'+productRequstesList + ']')
                else:
                    newProductRequstesLists.append('variables[' + productRequstesList + ']')

            product2 = dict(zip(newProductRequstesLists, productInformationList))

            productList.append(product2)

        return productList


    # 获取商品图片信息请求

    def getProductQueryDetail(self, productIds, method, url, headers):

        productDetailList = []

        for productId in productIds:
            params = {'variables[product_id]': productId}

            re = HttpRequest.http_request(method, url, params, headers)

            # 数据清理
            detail_html = re['result']['rows'][0]['detail_html']

            productDetailList.append(detail_html)

        return {'detail_html': productDetailList}

    # 获取商品规格信息请求
    def getSku(self, productIds, method, url, headers):

        productSku = []

        for productId in productIds:
            params = {'variables[product_id]': productId}

            re = HttpRequest.http_request(method, url, params, headers)
            # 数据清理
            productSku = re['result']['rows']

            productSku.append(productSku)

        return {'productSku': productSku}

    # 获取商品规格详细信息请求

    def getSkuList(self, productIds, method, url):

        productSkuList = []

        for productId in productIds:
            params = {'variables[product_id]': productId}

            re = HttpRequest.http_request(method, url, params)

            # 数据清理
            productSkuLists = re['result']['rows']

            productSkuList.append(productSkuLists)

        return {'productSkuList': productSkuList}




