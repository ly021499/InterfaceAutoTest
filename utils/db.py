#!/usr/bin/python
# @Time    : 2020/3/25 15:58
# @Author  : JACK
# @Desc  : 数据库操作
from utils.logger import log
import pymysql


class DB(object):

    def __init__(self, connections: tuple):
        self.connections = connections
        self.db = None
        self.cursor = None

    def connect_db(self):
        host, port, user, password = self.connections
        try:
            self.db = pymysql.connect(host=host, port=int(port), user=user, password=password)
            self.cursor = self.db.cursor()
            log.info("数据库连接成功, {}".format(self.db.host_info))
        except ConnectionError as e:
            log.error("数据库连接时发生错误, Error: {}".format(e), exc_info=True)
            raise e

    def execute_sql(self, sql):
        self.connect_db()
        log.info('执行Sql语句：{}'.format(sql))
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.db.commit()
            log.info('执行结果：{}'.format(result))
            return result
        except Exception as e:
            self.db.rollback()
            log.error("ERROR: 执行SQL语句时发生错误, 错误信息: {}".format(e))
        finally:
            self.close_db()

    def close_db(self):
        self.cursor.close()
        self.db.close()


