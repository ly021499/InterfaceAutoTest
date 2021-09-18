#!/usr/bin/python
# @Time  : 2020/4/20 14:37
# @Author: JACK
# @Desc  : HTTP请求方法
from utils.logger import log
import requests
import json
import time


class HttpRequest(object):

    def __init__(self):
        self.session = requests.session()

    def __call__(self, url, method, headers=None, data=None, **kwargs):
        """
        示例，可以直接通过类对象实例直接调用此方法
        request = HttpRequests()
        response = request(method, url, data)
        """
        return self.send_request(url, method, headers, data, **kwargs)

    def send_request(self, url, method, headers=None, data=None, **kwargs):
        """
        http 请求：
        :param url: 请求地址
        :param method: 请求方法
        :param headers: 请求头部
        :param data: 请求正文
        :return: response: 响应体
        """

        method_list = ["POST", "GET", "PUT", "PATCH"]
        method = method.upper()
        if method not in method_list:
            log.error("The request method is not supported!")
            raise BaseException

        log.info("Request URL: %s" % url)
        log.info("Request Method: [- %s -]" % method)
        log.info("Request Headers: %s" % headers)
        log.info("Request Body: %s" % data)

        response = None
        self.session.request(method, url, headers=headers, **kwargs)  # 需要规定params,data,json等传参格式
        if method == "POST":
            if headers["content-type"] == "application/x-www-form-urlencoded":
                response = self.session.post(url, data=data, headers=headers, timeout=20, **kwargs)
            elif headers["content-type"] == "application/json":
                response = self.session.post(url, json=data, headers=headers, timeout=20, **kwargs)
            elif headers["content-type"] == "multipart/form-data":
                response = self.session.post(url, file=data, headers=headers, timeout=20, **kwargs)
        elif method == "GET":
            response = self.session.get(url, params=data, headers=headers, timeout=20, **kwargs)
        elif method == "PUT":
            response = self.session.put(url, data=data, headers=headers, timeout=20, **kwargs)
        elif method == "PATCH":
            response = self.session.patch(url, data=data, headers=headers, timeout=20, **kwargs)

        start_timestamp = time.time()
        response_time_ms = round((time.time() - start_timestamp) * 1000, 2)

        try:
            response.raise_for_status()
            log.info('Response Json: %s' % response.json())
        except IOError as ex:
            log.error(f"{str(ex)}")
        else:
            log.info(
                f"Status Code: {response.status_code}  ,  "
                f"Response Time(ms): {response_time_ms} ms, "
            )

        return response



