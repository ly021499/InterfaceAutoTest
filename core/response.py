#!/usr/bin/python 
# @Time  : 2020/9/17 16:13
# @Desc  : HTTP响应处理
from utils.logger import log
from utils import tools
import json


class HttpResponse(object):

    def __init__(self, response=None):
        self.resp_obj = response
        self.resp_obj_meta = {
            "status_code": self.status_code,
            "headers": self.headers,
            "cookies": self.cookies,
            "content": self.content,
        }

    def __getattr__(self, key):
        if key in ["json", "content", "body"]:
            try:
                value = self.resp_obj.json()
            except ValueError:
                value = self.resp_obj.content
        elif key == "cookies":
            value = self.resp_obj.cookies.get_dict()
        else:
            try:
                value = getattr(self.resp_obj, key)
            except AttributeError:
                err_msg = "Response object does not have attribute: {}".format(key)
                log.error(err_msg)
                raise Exception(err_msg)

        self.__dict__[key] = value
        return value

    def _search_jsonpath(self, key):
        try:
            check_value = tools.get_target_value(obj=self.resp_obj_meta, key=key)
        except ValueError as ex:
            log.error(
                f"failed to search with jmespath\n"
                f"data: {self.resp_obj_meta}\n"
                f"exception: {ex}"
            )
            raise

        return check_value

    def extract_value(self, extractors):

        if not extractors:
            return {}

        extract_mapping = {}
        for key, field in extractors.items():
            field_value = self._search_jsonpath(key=field)
            extract_mapping[key] = field_value

        log.info(f"extract mapping:\n{json.dumps(extract_mapping, indent=4, ensure_ascii=False)}\n")

        return extract_mapping

    def validate(self, validators):

        if not isinstance(validators, list):
            return "Validator must be list type"

        log.info("Start to validate response.")

        for validator in validators:

            for comparator, expected in validator.items():

                try:

                    if comparator in ['equal', 'eq', 'Equal']:
                        assert expected[1] == tools.get_target_value(obj=self.resp_obj_meta, key=expected[0])

                    elif comparator in ['not_equal', 'not_eq', 'notEqual']:
                        assert expected[1] != tools.get_target_value(obj=self.resp_obj_meta, key=expected[0])

                    elif comparator in ['in', 'In']:
                        assert expected[0] in str(self.resp_obj_meta)

                    elif comparator in ['not_in', 'notIn']:
                        assert expected[0] not in str(self.resp_obj_meta)

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
    response = {'traceId': '46734a95898e412c9519a4b901abdc30',
                'status': '0',
                'msg': 'success',
                'token': '98e412c9519a4b901abdc30',
                'nickname': 'sara',
                'data': {
                    'nickname': 'link',
                    'jack': {
                        'nickname': 'jack'
                    }
                }
                }
    extractor = {'token': 'token', 'nickname': 'nickname-1'}
    res = HttpResponse(response)
    res.extract_value(extractor)