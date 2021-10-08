from core import client
import allure


@allure.feature("潭州电商")
@allure.story("商品模块")
class TestSample:

    @allure.title("查询我的合同")
    def test_query_contract(self):
        client.run_tests('query_contract.yaml')

    @allure.title("查询我的作业")
    def test_query_homework(self):
        client.run_tests('query_homework.yaml')


