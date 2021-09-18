#!/usr/bin/python 
# @Time  : 2021/5/20 17:39
# @Author: JACK
# @Desc  : 加载数据


class Loader:

    def __init__(self, yaml_path):
        self.yaml_path = yaml_path

    def load_data(self):
        pass


class Parser:

    def __init__(self, yaml_path):
        self.testcase = Loader(yaml_path)

    def parser_data(self):
        pass