#!/usr/bin/python
# @Time  : 2020/4/20 14:37
# @Author: JACK
# @Desc  : 断言封装
from utils.logger import log
from utils import tools


class Validator(object):

    def __init__(self, response):
        self.resp_obj = response

    def validate(self, validators):

        if not isinstance(validators, list):
            return "Validator must be list type"

        log.info("Start to validate response.")

        for validator in validators:

            for comparator, expected in validator.items():

                try:

                    if comparator in ['equal', 'eq', 'Equal']:
                        assert expected[1] == tools.get_target_value(obj=self.resp_obj, key=expected[0])

                    elif comparator in ['not_equal', 'not_eq', 'notEqual']:
                        assert expected[1] != tools.get_target_value(obj=self.resp_obj, key=expected[0])

                    elif comparator in ['in', 'In']:
                        assert expected[0] in str(self.resp_obj)

                    elif comparator in ['not_in', 'notIn']:
                        assert expected[0] not in str(self.resp_obj)

                    log.info(f"assert result: [Passed]\n"
                             f"comparator: {comparator}\n"
                             f"expected: {expected[-1]}\n"
                             )
                except AssertionError as ex:
                    log.error(f"assert result: [Failed]\n"
                              f"comparator: {comparator}\n"
                              f"expected: {expected[-1]}\n"
                              )
                    raise ex


if __name__ == '__main__':
    validator = [{'Equal': ['status', '0']}, {'not_in': ['status1']}]

    response = {'traceId': '46734a95898e412c9519a4b901abdc30',
                'status': '0',
                'msg': 'success'
                }
    Validator(response).validate(validator)
