#!/usr/bin/python
# @Time    : 2020/3/25 15:58
# @Author : JACK
# @Desc  : 工具函数
from string import Template
import jsonpath
import json
import os
import shutil
import config


def replace_data(raw_var, global_data):
    """
    数据替换方法
    :param raw_var: str, 原字符串对象，例如dict类型的请求参数转换后的str类型数据
    :param global_data: dict, 字典类型，替换的数据，例如公共字典或其他
    :return:
    """
    if not isinstance(raw_var, str):
        raise TypeError('raw_var must be str！')

    template = Template(raw_var)
    data = template.safe_substitute(global_data)
    try:
        data = json.loads(data)
    except:
        data = eval(data)
    return data


def get_target_value(obj, key):
    """
    获取JSON数据中的指定key的value值
    :param obj: dict, 字典对象
    :param key: str, 键名
    :return:
    """
    if not isinstance(obj, dict):
        return "TypeError: unexpected types, Only Supported Dictionary"

    # 当值不唯一时，通过.分割字符串，取对应索引的值
    if "." in str(key):
        value, index = str(key).split('.')
    else:
        value = key
        index = 0
    expr = '$..{}'.format(str(value))

    field_value = jsonpath.jsonpath(obj=obj, expr=expr)[int(index)]

    return field_value


def open_allure():
    """
    运行完后，自动打开 allure 报告
    :return:
    """

    # 复制environment.properties文件
    raw_file_path = os.path.join(config.REPORT_DIR, 'environment.properties')
    new_file_path = os.path.join(config.REPORT_DIR, 'output/environment.properties')

    shutil.copy(raw_file_path, new_file_path)

    output_dir = os.path.join(config.REPORT_DIR, 'output')
    summary_dir = os.path.join(config.REPORT_DIR, 'summary')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    if not os.path.exists(summary_dir):
        os.mkdir(summary_dir)

    generate_allure_cmd = "allure generate {} -o {} --clean".format(output_dir, summary_dir)
    os.system(generate_allure_cmd)

    open_allure_cmd = "allure open {}".format(summary_dir)
    os.system(open_allure_cmd)


if __name__ == '__main__':
    open_allure()