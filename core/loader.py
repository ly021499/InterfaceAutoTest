#!/usr/bin/python 
# @Time  : 2021/5/20 17:39
# @Author: JACK
# @Desc  : 数据操作文件
import yaml
from utils.logger import log


def load_path(filepath):
    filepath_list = []
    if os.path.isfile(filepath):
        filepath_list.append(filepath)
        return
    if os.path.isdir(filepath):
        folder = filepath
        for root, dirs, files in os.walk(folder):
            for file in files:
                if not file.endswith(('yaml', 'yml')):
                    continue

                filepath_list.append(os.path.join(root, file))
    return filepath_list


def load_yaml(filepath):
    with open(filepath, encoding='utf-8') as file:
        try:
            stream = yaml.safe_load(file)
        except yaml.YAMLError as ex:
            log.error(str(ex))
            raise ex

        return stream


def parser_config(config):
    from config import Config
    variables = config.get(Config.ENV.lower())
    from utils.const import Const
    const = Const.global_val()
    const.update(**variables)
    log.info("parser config variables: {}".format(variables))
    return const


if __name__ == '__main__':
    from config import Config
    import os
    yaml_path = os.path.join(Config.DATA_DIR, 'login_account.yaml')
    data = load_yaml(yaml_path)
    print(data)