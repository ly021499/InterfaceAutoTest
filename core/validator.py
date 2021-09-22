#!/usr/bin/python 
# @Time  : 2020/9/19 10:13
# @Author: JACK
# @Desc  : 断言方法
from utils import tools
from utils.logger import log


class Validator(object):

    def __init__(self, response, validator):
        self.validators = validator
        self.response = response

    def validate(self):

        if not self.validators and not isinstance(self.validators, (list, dict)):
            return "Validator must be ff dict or list type"

        log.info("Start to validate response.")

        for validator in self.validators:
            for comparator, expected in validator.items():
                if comparator in ['eq', 'equal']:
                    assert expected[1] == tools.get_target_value(obj=self.response, key=expected[0])
                elif comparator in ['notEqual', 'not_equal']:
                    assert expected[1] != tools.get_target_value(obj=self.response, key=expected[0])
                elif comparator == 'in':
                    assert expected[0] in str(self.response)
                elif comparator in ['notIn', 'not_in']:
                    assert expected[0] not in str(self.response)
                log.info("Assert result: [Passed]  comparator: {}  expected: {} ".format(comparator, expected))

                # if isinstance(expected, dict):
                #     for key, expected_value in expected.items():
                #         if comparator in ['eq', 'equal']:
                #             assert expected_value == tools.get_target_value(obj=self.response, key=key)
                #         elif comparator in ['notEqual', 'not_equal']:
                #             assert expected_value != tools.get_target_value(obj=self.response, key=key)
                # elif isinstance(validator, list):
                #     if comparator == 'in':
                #         assert expected in str(self.response)
                #     elif comparator in ['notIn', 'not_in']:
                #         assert expected not in str(self.response)
                # log.info("Assert result: [Passed]  comparator: {}  expected: {} ".format(comparator, expected))


if __name__ == '__main__':
    res = {
    "traceId": "9b7539b8dcdf4a529f8cb62fc4760e17",
    "status": "0",
    "msg": "success",
    "data": {
        "user": {
            "uid": 2338240,
            "mobile": "15131424735",
            "account": "m15131424735",
            "nickname": "Jack",
            "headImg": "https://res.shiguangkey.com/file/202007/20/20200720192553054460756.jpg",
            "openId": "",
            "newRegister": False,
            "needBindPhone": False,
            "showAccountList": False
        },
        "token": "eb93a0490623adc098e540d4955951df"
    }
    }
    validators = [{'equal': ['msg', 'success']}, {'not_in': ['statuss']}]
    va = Validator(validators, res)
    va.validate()