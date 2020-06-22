
from Fxm.getProduct.getProductQuery import getProductQuery
from Fxm.data.rwYaml import writeDate, readYaml


from Fxm.data.readRequestParameter import getUrl, getHeaders

def testProduct():
    # #
    productRequstesLists = ['business', 'name', 'status','min_limit_count',
                            'limit_count', 'country', 'province', 'city', 'pay_ways', 'img_main',
                            'img_main_small', 'img_poster', 'img_list', 'begin_time', 'end_time',
                            'off_shelf_time', 'is_show_countdown', 'countdown_value', 'is_sub_wechat',
                            'img_poster_type', 'class', 'is_display_pageviews']

    size = 20
    url = getUrl()[0]['url']
    headers = getHeaders()[0]
    method = getUrl()[0]['method']


    gtq = getProductQuery()
    name = getProductQuery().productQuery.__name__

    r = gtq.productQuery(size, method, url, headers, productRequstesLists)
    writeDate(r, name)


def test_querydetail():
    productIds = readYaml('DataproductID.yaml')


    url = getUrl()[1]['url']
    headers = getHeaders()[0]
    method = getUrl()[1]['method']

    gtq = getProductQuery()
    name = getProductQuery().getProductQueryDetail.__name__

    r = gtq.getProductQueryDetail(productIds, method, url, headers)
    writeDate(r, name)


def test_sku():
    productIds = readYaml('DataproductID.yaml')

    url = getUrl()[2]['url']
    headers = getHeaders()[0]
    method = getUrl()[2]['method']

    gtq = getProductQuery()
    name = getProductQuery().getSku.__name__

    r = gtq.getSku(productIds, method, url, headers)
    writeDate(r, name)

def test_sku_list():
    productIds = readYaml('DataproductID.yaml')

    url = getUrl()[3]['url']
    headers = getHeaders()[0]
    method = getUrl()[3]['method']

    gtq = getProductQuery()
    name = getProductQuery().getSkuList.__name__

    r = gtq.getSkuList(productIds, method, url)
    writeDate(r, name)



def test():

    productDitail = readYaml("DatagetProductQueryDetail.yaml")

    print(productDitail['detail_html'])








