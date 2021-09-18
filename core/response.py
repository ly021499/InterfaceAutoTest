#!/usr/bin/python 
# @Time  : 2021/9/17 16:13
# @Desc  : 处理HTTP响应信息
from utils.logger import log
from utils.tools import get_target_value
import jmespath


class HttpResponse(object):

    def __init__(self, response):
        self.resp_obj = response
        self.resp_obj_meta = {
            "status_code": self.status_code,
            "headers": self.headers,
            "cookies": self.cookies,
            "body": self.body,
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
                err_msg = "ResponseObject does not have attribute: {}".format(key)
                log.error(err_msg)
                raise Exception(err_msg)

        self.__dict__[key] = value
        return value

    def _search_jmespath(self, expr):
        try:
            check_value = jmespath.search(expr, self.resp_obj_meta)
        except ValueError as ex:
            log.error(
                f"failed to search with jmespath\n"
                f"expression: {expr}\n"
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
            field_value = self._search_jmespath(field)
            extract_mapping[key] = field_value

        log.info(f"Extract Mapping: {extract_mapping}")
        return extract_mapping

    def search_jsonpath(self, extractors):

        if not extractors:
            return {}

        extract_mapping = {}

        for key, value in extractors.items():

            field_value = get_target_value(obj=self.resp_obj_meta, key=value)
            extract_mapping[key] = field_value

        log.info(f"Extract Mapping: {extract_mapping}")
        return extract_mapping

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