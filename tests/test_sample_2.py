from core import client
import allure


@allure.feature("潭州课堂")
@allure.story("订单模块")
class TestSample2:

    @allure.title("查询我的信息")
    def test_query_mine(self):
        client.quick_request('query_mine.yaml')

    @allure.title("查询我的订单")
    def test_query_order(self):
        client.quick_request('query_order.yaml')
