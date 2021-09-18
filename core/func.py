#!/usr/bin/python 
# @Time  : 2021/5/18 21:27
# @Author: JACK
# @Desc  : 文件描述信息
import jsonpath
import json
from string import Template
from core.config.config_log import logger

log = logger


def replace_data(raw_var, global_data):
    raw_var = str(raw_var)

    if not isinstance(raw_var, str):
        raise TypeError('raw_var must be str！')

    template = Template(raw_var)
    data = template.safe_substitute(global_data)
    try:
        data = json.loads(data)
    except:
        data = eval(data)
    return data


def quick_request(data, **kwargs):
    new_data = oyaml.rafactor_data(data)
    desc, url, method, header, param, extract, check = new_data

    log.info('TestCase Desc: %s' % desc)

    params = replace_data(param, G_VAR)

    if kwargs:
        params = dict(params, **kwargs)

    response = RequestObject().send_request(url, method, header, params)
    extract_value = ResponseObject(response).search_jsonpath(extract)
    G_VAR.update(extract_value)

    return response.json()
