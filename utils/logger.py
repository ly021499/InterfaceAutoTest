#!/usr/bin/python
# @Time  : 2020/3/25 16:01
# @Desc  : 日志文件
import logging
import time
from logging.handlers import TimedRotatingFileHandler
from config import Config
import os


class Logger(object):
    """
    终端打印不同颜色的日志，在pycharm中如果强行规定了日志的颜色， 这个方法不会起作用， 但是
    对于终端，这个方法是可以打印不同颜色的日志的。
    """

    # 在这里定义StreamHandler，可以实现单例， 所有的logger()共用一个StreamHandler
    ch = logging.StreamHandler()

    def __new__(cls, *args, **kwargs):
        """
        实现只有一个对象
        :param args:
        :param kwargs:
        :return:
        """
        if not hasattr(cls, '_instance'):
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = '[%(asctime)s] - [%(levelname)s] - %(message)s'

        # if not self.logger.handlers:
        #     # 构建日志路径结构
        #     date = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
        #     log_path = os.path.join(Config.BASE_DIR, "report/log")
        #     if not os.path.exists(log_path):
        #         os.mkdir(log_path)
        #
        #     # 完整日志存放路径
        #     all_log_path = os.path.join(log_path, "all_log")
        #     all_log_name = all_log_path + "/" + date + ".log"
        #     if not os.path.exists(all_log_path):
        #         os.mkdir(all_log_path)
        #
        #     # 错误日志存放路径
        #     error_log_path = os.path.join(log_path, "error_log")
        #     error_log_name = error_log_path + "/" + date + ".log"
        #     if not os.path.exists(error_log_path):
        #         os.mkdir(error_log_path)
        #
        #     # 创建一个handler,用于写入日志文件
        #     fh = logging.FileHandler(all_log_name, encoding='utf-8')
        #     fh.setLevel(logging.INFO)
        #
        #     # 定义handler的输出格式
        #     formatter = logging.Formatter(self.formatter)
        #     fh.setFormatter(formatter)
        #
        #     # 给logger添加handler
        #     self.logger.addHandler(fh)
        #
        #     # 错误日志写入Handler
        #     eh = TimedRotatingFileHandler(filename=error_log_name, when="midnight",
        #                                   backupCount=3, interval=1, encoding="utf-8")
        #     eh.setLevel(logging.ERROR)
        #     eh.setFormatter(formatter)
        #     self.logger.addHandler(eh)

    def debug(self, message):
        self.set_color_formatter('\033[0;34m%s\033[0m')
        self.logger.debug(message)

    def info(self, message):
        self.set_color_formatter('\033[0;32m%s\033[0m')
        self.logger.info(message)

    def warning(self, message):
        self.set_color_formatter('\033[0;33m%s\033[0m')
        self.logger.warning(message)

    def error(self, message):
        self.set_color_formatter('\033[0;35m%s\033[0m')
        self.logger.error(message)

    def critical(self, message):
        self.set_color_formatter('\033[0;31m%s\033[0m')
        self.logger.critical(message)

    def set_color_formatter(self, color):
        # 不同的日志输出不同的颜色
        formatter = logging.Formatter(color % self.formatter)
        self.ch.setFormatter(formatter)
        self.ch.setLevel(logging.INFO)
        self.logger.addHandler(self.ch)


log = Logger()

if __name__ == '__main__':
    log.info("12345")
    log.debug("12345")
    log.warning("12345")
    log.error("12345")
    log.critical("12345")



