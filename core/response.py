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
                err_msg = "responseObject does not have attribute: {}".format(key)
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
            field_value = get_target_value(obj=self.resp_obj_meta, key=field)
            extract_mapping[key] = field_value

        log.info(f"extract mapping: {extract_mapping}")
        return extract_mapping
