#!/usr/bin/python 
# @Time  : 2021/5/18 21:27
# @Author: JACK
# @Desc  : 函数封装
from utils import tools
from core.validator import Validator
from core import loader
from core.response import HttpResponse
from core.session import HttpRequest


def quick_request(filename):
    file_data = loader.load_yaml(filepath=filename)
    config_var = file_data.pop(0)['config']
    g_var = loader.parser_config(config_var)
    for api in file_data:
        # 获取HTTP请求常用数据
        method, url, name = api['method'], api['url'], api['name']
        request = tools.replace_data(str(api['request']), g_var)
        # 发起HTTP请求
        response = HttpRequest().send_request(method=method, url=url, name=name, **request)
        # 处理响应内容
        resp = HttpResponse(response)
        # 断言处理
        validator = api['validate']
        if validator:
            resp.validate(validator)
        # 提取数据
        extractor = api.get('extract')
        if extractor:
            extract_variable = resp.extract_value(extractor)
            g_var.update(extract_variable)


if __name__ == '__main__':
    import config
    import os
    yaml_path = os.path.join(config.DATA_DIR, 'query_contract.yaml')
    quick_request(yaml_path)