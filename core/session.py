#!/usr/bin/python
# @Time  : 2020/4/20 14:37
# @Author: JACK
# @Desc  : HTTP请求处理
from utils.logger import log
import requests
import json
from requests import exceptions
import time


class HttpRequest(object):

    def __init__(self):
        self.session = requests.session()

    def __call__(self, method, url, name, **kwargs):
        """
        示例，可以直接通过类对象实例直接调用此方法
        request = HttpRequests()
        response = request(method, url, data)
        """
        return self.send_request(url, method, name, **kwargs)

    def send_request(self, method, url, name, **kwargs):
        """
        http 请求方法
        :param method: 请求方法
        :param url: 请求地址
        :param name: 接口名称
        :return: response: 响应体
        """

        method_list = ["POST", "GET", "PUT", "PATCH"]
        method = method.upper()

        if method not in method_list:
            log.error("the request method is not supported!")
            raise BaseException

        identifier = ' = ' * 6
        log.info(f"processed request: {name}")
        log.info(f"{identifier} request detail {identifier}")
        log.info(f"> [{method}] {url}")
        kwarg = kwargs.copy()
        if kwarg.get('headers'):
            log.info(f"> headers: {kwarg.pop('headers')}")
        log.info(f"parameter: \n{json.dumps(kwarg, indent=4, ensure_ascii=False)}")

        kwargs.setdefault("timeout", 10)

        start_timestamp = time.time()
        response = self.session.request(method, url, **kwargs)  # 需要规定params,data,json等传参格式
        response_time_ms = round((time.time() - start_timestamp) * 1000, 2)

        try:
            response.raise_for_status()
            log.info(f'> = = = = response detail = = = = \n{json.dumps(response.json(), indent=4, ensure_ascii=False)} ')
        except (exceptions.MissingSchema, exceptions.InvalidSchema, exceptions.InvalidURL):
            raise
        else:
            log.info(
                f"status code: {response.status_code}  ,"
                f"response time(ms): {response_time_ms} ms\n"
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
    res = HttpRequest().send_request(methods, urls, name="LOUIE测试接口", headers=header, data=data)
    from core.response import HttpResponse
    r = HttpResponse(res)
    from utils.tools import get_target_value
    value = get_target_value(obj=r.resp_obj_meta, key='msg')
