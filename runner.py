#!/usr/bin/python
# @Time  : 2020/9/17 16:43
# @Author: JACK
# @Desc  : 程序执行入口
from utils import tools
from utils.logger import log
import config
import os
import sys
import pytest


def add_arguments():
    args = sys.argv[1:][0].split('--')[1].lower()
    arguments = ['test', 'prod', 'fat', 'pre']
    if args not in arguments:
        help_text = """
        prompt: only four environment parameters are supported\n
        :params: --test
        :params: --fat
        :params: --pre
        :params: --prod
        """
        print(help_text)
        log.error(help_text)
        return
    else:
        config.ENV = args
        print('Current Operating Environment:  {}'.format(config.ENV))
        log.info(f'Current Operating Environment:{config.ENV}\n')


def main(env=None):
    if env:
        add_arguments()
    else:
        if env is None:
            env = 'prod'
        config.ENV = env

    output_dir = os.path.join(config.REPORT_DIR, 'output')
    options = ["--alluredir={}".format(output_dir), "--clean-alluredir", config.CASE_DIR]
    log.info("options list: {}".format(options))

    log.info(" = " * 8 + " Process started, Running tests  " + " = " * 8)
    pytest.main(options)
    log.info(" = " * 8 + " Process finished, Testing is completed " + " = " * 8)

    # tools.open_allure()


if __name__ == '__main__':
    main()
