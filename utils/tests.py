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


def test_pri(self):
    assert 0 == 0


TestSequense = type('TestSequense', (object,), {})
setattr(TestSequense, 'test_pri', test_pri)
print(TestSequense.__dict__)


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '--co'])