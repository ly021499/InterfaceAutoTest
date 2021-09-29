#!/usr/bin/python
# @Time  : 2020/9/17 16:43
# @Author: JACK
# @Desc  : 程序执行入口
from utils import tools
from utils.logger import log
import config
import os
import pytest


def run(path=None):
    if not path:
        path = config.CASE_DIR

    output_dir = os.path.join(config.REPORT_DIR, 'output')
    options = ["--alluredir={}".format(output_dir), "--clean-alluredir", path]
    log.info("options list: {}".format(options))

    log.info(" = " * 8 + " Process started, Running tests  " + " = " * 8)
    pytest.main(options)
    log.info(" = " * 8 + " Process finished, Testing is completed " + " = " * 8)

    tools.open_allure()


if __name__ == '__main__':
    run()