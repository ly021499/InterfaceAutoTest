#!/usr/bin/python
# @Time  : 2020/4/20 14:37
# @Author: JACK
# @Desc  : HTTP请求方法
from utils.logger import log
import requests
from requests import exceptions
import time


class HttpRequest(object):

    def __init__(self):
        self.session = requests.session()

    def __call__(self, url, method, name, **kwargs):
        """
        示例，可以直接通过类对象实例直接调用此方法
        request = HttpRequests()
        response = request(method, url, data)
        """
        return self.send_request(url, method, name, **kwargs)

    def send_request(self, url, method, name, **kwargs):
        """
        http 请求：
        :param url: 请求地址
        :param method: 请求方法
        :param headers: 请求头部
        :param name: 接口名称
        :return: response: 响应体
        """

        method_list = ["POST", "GET", "PUT", "PATCH"]
        method = method.upper()

        if method not in method_list:
            log.error("The request method is not supported!")
            raise BaseException

        log.info("processed request: {}".format(name))
        log.info("> [{method}] {url}".format(method=method, url=url))
        # log.info("> headers: {headers}".format(headers=headers))
        log.info("> kwargs: {kwargs}".format(kwargs=kwargs))

        kwargs.setdefault("timeout", 10)

        start_timestamp = time.time()
        response = self.session.request(method, url, **kwargs)  # 需要规定params,data,json等传参格式
        response_time_ms = round((time.time() - start_timestamp) * 1000, 2)

        try:
            response.raise_for_status()
            log.info('response json: %s' % response.json())
        except (exceptions.MissingSchema, exceptions.InvalidSchema, exceptions.InvalidURL):
            raise
        else:
            log.info(
                f"status code: {response.status_code}  ,"
                f"response time(ms): {response_time_ms} ms"
            )

        return response


if __name__ == '__main__':
    urls = 'https://open.shiguangkey.com/api/udb/login/standard'
    header = {
        "content-type": "application/x-www-form-urlencoded",
        "terminaltype": "4"
    }
    methods = 'post'
    data = {
        'account': 'm15131424735',
        'password': 'xu9o8rj118541WgRNyP7DA'
    }
    res = HttpRequest()(urls, methods, header, "LOUIE测试接口", data=data)
    print(res)