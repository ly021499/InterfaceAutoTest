#!/usr/bin/python 
# @Time  : 2020/5/20 17:39
# @Author: JACK
# @Desc  : 数据加载
import yaml
import os
import config
from utils.logger import log
from utils.const import Const


def load_folder(folder):
    filepath_list = []

    if os.path.isdir(folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                if not file.endswith(('yaml', 'yml')):
                    continue

                filepath_list.append(os.path.join(root, file))
    return filepath_list


def load_yaml(filepath):
    """
    读取指定YAML文件数据
    :param filepath:
    :return:
    """
    filepath = os.path.join(config.DATA_DIR, filepath)
    with open(filepath, encoding='utf-8') as file:
        try:
            stream = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise e

        return stream


def parser_config(config_var):
    variables = config_var.get(config.ENV.lower())

    const = Const.global_val()
    const.update(**variables)

    log.info("parser config variables: {}".format(variables))
    return const


