#!/usr/bin/python 
# @Time  : 2020/9/19 10:13
# @Author: JACK
# @Desc  : 断言方法
from utils import tools
from utils.logger import log


class Validator(object):

    @staticmethod
    def assert_equal(res, dic):
        """断言是否相等"""
        for k, v in dic.items():
            actual_value = tools.get_target_value(obj=res, key=k)
            expect_value = v
            log.info('断言类型：[@相等] - 预期值：({})  ==  实际值：({})'.format(expect_value, actual_value))
            assert str(actual_value) == str(expect_value)

    @staticmethod
    def assert_not_equal(res, dic):
        """断言不相等"""
        for k, v in dic.items():
            actual_value = tools.get_target_value(res, k)
            expect_value = v
            try:
                assert actual_value != str(expect_value)
                log.info('断言类型：[@不相等] - 预期值：({})  !=  实际值：({})'.format(expect_value, actual_value))
            except AssertionError as e:
                log.error('断言类型：[@不相等] - 预期值：({})  !=  实际值：({})'.format(expect_value, actual_value))
                raise e

    @staticmethod
    def assert_in(res, *string):
        """断言是否存在"""
        for str_ in string:
            assert str(str_) in str(res)
            log.info('断言类型：[@存在] - 预期：({}) in RES 中'.format(str_))

    @staticmethod
    def assert_not_none(res, key):
        """断言是否为空"""
        value = tools.get_target_value(res, key)
        if value:
            log.info('断言类型：[@不为空] - 预期：({}) is not None'.format(key, value))
        else:
            raise AssertionError

    @staticmethod
    def assert_true(res, key):
        """断言是否为True"""
        value = tools.get_target_value(res, key)
        assert bool(value) is True
        log.info('断言类型：[@为True]， 预期：({}) is True'.format(key, value))
