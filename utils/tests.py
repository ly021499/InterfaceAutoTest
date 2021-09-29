#!/usr/bin/python
# @Time    : 2020/3/25 15:58
# @Author : JACK
# @Desc  : 调试文件


class HTTP(object):

    def __init__(self):
        pass

    def __getattribute__(self, item):
        if item in ['json', 'content', 'body']:
            return '222222222'
        else:
            return '11111111111'

    def __getattr__(self, item):
        if item in ['json', 'content', 'body']:
            return 'jackjson'
        elif item == 'cookies':
            return 'jackcookie'
        else:
            return 'jackgg'

    def __dict__(self):
        pass


dic = {'a': 'b', 'v': 'b'}
for k,v in dic.items():
    print({k, v})