import requests
class HttpRequest:
    '''
    利用request封装get请求和post请求
    '''

    def http_request(method, url, data, headers=None):

        '''
        :param
        @url:请求的地址
        @param:传递的参数 非必填参数 字典格式传递参数
        :return
        返回一个消息实体
        '''
        if method == "get":
            response = requests.get(url, params=data, headers=headers)
        elif method == "post":
            response = requests.post(url, params=data, headers=headers)
        else:
            return 0
        return response.json()