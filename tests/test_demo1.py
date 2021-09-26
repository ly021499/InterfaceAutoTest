#!/usr/bin/python 
# @Time  : 2021/9/17 16:43
# @Desc  : 文件描述信息
from core.client import quick_request
import pytest


class TestDemo:

    def test_query_contract(self, load_all_yaml):
        for yaml_path in load_all_yaml:
            quick_request(yaml_path)


if __name__ == '__main__':
    # print(filepath_list)
    pytest.main([__file__, '--html=./report/', '-s'])
