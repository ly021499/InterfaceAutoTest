#!/usr/bin/python 
# @Time  : 2021/5/18 21:27
# @Author: JACK
# @Desc  : 文件描述信息
from utils import tools
from core.validator import Validator
from core import loader
from core.response import HttpResponse
from core.session import HttpRequest


def quick_request(filename):
    file_data = loader.load_yaml(filename)
    config = file_data.pop(0)['config']
    const = loader.parser_config(config)
    for i in file_data:
        request = tools.replace_data(str(i.get('request')), const)
        response = HttpRequest().send_request(i['url'], i['method'], i.get('name'), **request)
        res_obj = HttpResponse(response)
        validator = i.get('validate')
        Validator(response.json(), validator).validate()
        extract = i.get('extract')
        extract_variable = res_obj.extract_value(extract)
        const.update(**extract_variable)


if __name__ == '__main__':
    from config import Config
    import os
    yaml_path = os.path.join(Config.DATA_DIR, 'login_account.yaml')
    quick_request(yaml_path)