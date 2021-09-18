#!/usr/bin/python
# @Time    : 2020/3/25 15:58
# @Author  : JACK
# @Desc  : 存放全局变量
from utils import factory


class Const:

    @classmethod
    def global_val(cls):
        val = {
            'timestamp': factory.timestamp(),
            'today_start_timestamp': factory.today_start_timestamp(),
            'today_end_timestamp': factory.today_end_timestamp(),
        }
        return val.copy()


if __name__ == '__main__':
    print(Const.global_val())
    import time
    time.sleep(2)



