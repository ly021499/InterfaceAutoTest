#!/usr/bin/python 
# @Time  : 2020/9/19 10:13
# @Author: JACK
# @Desc  : 断言方法
from utils import tools
from utils.logger import log


class Validator(object):

    def __init__(self, validator):
        self.validator = validator

    def validate(self):
        if not self.validator and not isinstance(self.validator, dict):
            return "Validator Must Be Of Dict Type"
        for validate_type, expected in self.validator:
            for k, v in expected:
                if k in ['eq', 'equal']:
                    pass
                if k == 'in':
                    pass
                if k == 'notIn':
                    pass

    def validate(self, validator):
        """
        :param validator: YAML文件中的 check 节点数据
        :return: None
        """

        code = ['code', 'status', 'res', 'msg']
        entity = ['data', 'result']

        if validator == "no_check" or validator is None:
            log.info("This Case Has No Check!")

        if not isinstance(validator, dict):
            log.info("Check Must Be Of Dict Type")

        else:

            for key, value in check.items():

                if key in code:
                    actual_code = self.resp_obj[key]
                    expect_code = check[key]
                    assert str(actual_code) == str(expect_code)
                    log.info('校验类型: [-{}], 结果: [Passed], 预期: [{}]'.format(key, str(expect_code)))

                if key in entity:
                    data = self.resp_obj[key]

                    for check_param in check["data"]:
                        if isinstance(check_param, dict):

                            for assert_type, expect_value in check_param.items():
                                if assert_type == 'in':
                                    assert expect_value in str(data)

                                if assert_type == 'not_in':
                                    assert expect_value not in str(data)

                                if assert_type == 'eq':
                                    for p, o in expect_value.items():
                                        assert assert_type == self.search_jsonpath(data, p)

                                if assert_type == 'not_none':
                                    avalue = self.search_jsonpath(data, expect_value)
                                    assert avalue is not None

                                log.info('校验类型: [-{}]  结果: [Passed]  预期: {}'.format(assert_type, expect_value))

                        elif isinstance(check_param, str):
                            assert check_param in str(data)
                            log.info('校验类型: [-in]  结果: [Passed]  预期: [{}]'.format(check_param))

                        else:
                            print('请输入正确校验数据格式！！')

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
