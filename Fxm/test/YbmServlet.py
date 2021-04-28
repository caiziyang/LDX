import requests
import time
import random


def YbmServlet():
    url = 'https://www.eeagd.edu.cn/crxwwy/YbmServlet?' \
          'ksid=528781&xm=%E8%94%A1%E5%AD%90%E6%89%AC&xbdm=' \
          '1&pwd=qq873216&mzdm=01&csrq=1995-11-02&zzmmdm=13&zj' \
          'lxdm=1&zjdm=441723199511022014&yzbm=' \
          '&lxdh=&lxsj=13128629906' \
          '&txdz=%E5%B9%BF%E5%B7%9E%E5%B8%82%E7%95' \
          '%AA%E7%A6%BA%E5%8C%BA%E5%B8%82%E6%A1%A5%E6%' \
          'B2%99%E5%A4%B4%E6%9D%91%E6%96%B0%E5%9F%BA%E5%A4%A7%E8%A1%97' \
          '&xxxsdm=4&zxztdm=2&' \
          'byxx=%E5%8D%8E%E5%8D%97%E5%B8%88%E8%8C%' \
          '83%E5%A4%A7%E5%AD%A6&byrq=2021-12-31&byzy=%' \
          'E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6' \
          '%E4%B8%8E%E6%8A%80%E6%9C%AF&yxdm=10574&wyyzdm=1' \
          '&yxzydm=010&czbj=1&xhOrZkh=44641922310002&kddm=1057402'

    headers = {'Cookie': 'BIGipServercrxwwy_pool=3379494922.16927.0000; '
                         'BIGipServerzk_pool=365428746.20480.0000; '
                         'BIGipServerportal_redirect_pool=1768882186.36895.0000;'
                         ' JSESSIONID=STgPW-CN0sIWJ8m3Mor6PVywTZUJBCbXqwB-LX6Ga-HKFQxWlovZ!-1133595419!-1502077985',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
    data = {}
    res = requests.post(url=url, data=data, headers=headers)
    return res.json()


if __name__ == '__main__':
    for i in range(1000000):
        times = random.randint(1, 10) * 0.1
        time.sleep(times)
        ybm_servlet = YbmServlet()
        if ybm_servlet['msg'] != '修改失败:该考点1057402报考人数已满,请选择其他考点！':
            print(ybm_servlet)
            break
    print("结束！！！")