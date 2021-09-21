#!/usr/bin/python 
# @Time  : 2021/5/20 17:39
# @Author: JACK
# @Desc  : 数据操作文件
import yaml
import os


class Loader:

    def __init__(self):
        self.stream_list = []
        self.filepath_list = []

    def load_path(self, filepath):
        if os.path.isfile(filepath):
            self.filepath_list.append(filepath)
            return
        if os.path.isdir(filepath):
            file_dir = filepath
            for root, dirs, files in os.walk(file_dir):
                for file in files:
                    if str(file).endswith('.yaml'):
                        self.filepath_list.append(os.path.join(root, file))

    def load_data(self):
        for filepath in self.filepath_list:
            with open(filepath, encoding='utf-8') as file:
                stream = yaml.safe_load(file)
            self.stream_list.append(stream)


class Parser:

    def __init__(self, filepath):
        self.testcase = Loader(filepath)

    def parser_data(self):
        pass


if __name__ == '__main__':
    from config import Config
    import os
    yaml_path = os.path.join(Config.DATA_DIR, 'login_account.yaml')
    loader = Loader()
    loader.load_path(Config.DATA_DIR)
    loader.load_data()
    for i in loader.stream_list:
        print()
        print(i)
