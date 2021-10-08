#!/usr/bin/python
# @Time  : 2021/5/18 18:12
# @Author: JACK
# @Desc  : 配置文件
import platform
import os


ENV = 'prod'
SYSTEM = platform.system()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CASE_DIR = os.path.join(BASE_DIR, "tests")
REPORT_DIR = os.path.join(BASE_DIR, "report")



