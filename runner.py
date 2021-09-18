#!/usr/bin/python
# @Time  : 2021/9/17 16:43
# @Author: JACK
# @Desc  : 程序执行入口
from utils import tools
from utils.logger import log
from config import Config
import os
import pytest


def run(path):
    output_dir = os.path.join(Config.REPORT_DIR, 'output')
    options = [output_dir, "--clean-alluredir", 'no:warnings', path]
    log.info(options)
    log.info(" = " * 8 + " 程序开始运行， 测试开始 " + " = " * 8)
    pytest.main(options)
    log.info(" = " * 8 + " 程序停止运行， 测试结束 " + " = " * 8)
    tools.open_allure()
