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
    yaml_data = loader.load_yaml(filename)
    config_var = yaml_data.pop(0)['config']
    variable = loader.parser_config(config_var)
    for data in yaml_data:
        request = tools.replace_data(str(data.get('request')), variable)
        response = HttpRequest().send_request(data['url'], data['method'], data.get('name'), **request)
        res_obj = HttpResponse(response)
        validator = data.get('validate')
        Validator(response.json(), validator).validate()
        extract = data.get('extract')
        extract_variable = res_obj.extract_value(extract)
        variable.update(**extract_variable)


if __name__ == '__main__':
    import config
    import os
    yaml_path = os.path.join(config.DATA_DIR, 'login_account.yaml')
    quick_request(yaml_path)