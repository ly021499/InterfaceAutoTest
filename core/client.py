#!/usr/bin/python 
# @Time  : 2021/5/18 21:27
# @Author: JACK
# @Desc  : 函数封装
from utils import tools
from core import loader
from core.response import HttpResponse
from core.session import HttpRequest


def run_tests(filename):
    tests_dict = loader.load_yaml(filepath=filename)
    config_data = tests_dict.pop(0)['config']
    config_dict = loader.parser_config(config_data)
    for test in tests_dict:
        # 获取HTTP请求常用数据
        method, url, name = test['method'], test['url'], test['name']
        request = tools.replace_data(str(test['request']), config_dict)
        # 发起HTTP请求
        response = HttpRequest().send_request(method=method, url=url, name=name, **request)
        # 处理响应内容
        resp = HttpResponse(response)
        # 断言处理
        validator = test['validate']
        if validator:
            resp.validate(validator)
        # 提取数据
        extractor = test.get('extract')
        if extractor:
            extract_variable = resp.extract_value(extractor)
            config_dict.update(extract_variable)


if __name__ == '__main__':
    import config
    import os
    yaml_path = os.path.join(config.DATA_DIR, 'query_contract.yaml')
    run_tests(yaml_path)