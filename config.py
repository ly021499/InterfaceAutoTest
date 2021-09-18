#!/usr/bin/python
# @Time  : 2021/5/18 18:12
# @Author: JACK
# @Desc  : 配置文件
import platform
import os


class Config:

    SYSTEM = platform.system()
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    CASE_DIR = os.path.join(BASE_DIR, "tests")
    REPORT_DIR = os.path.join(BASE_DIR, "report")


if __name__ == '__main__':
    print(Config.BASE_DIR)
