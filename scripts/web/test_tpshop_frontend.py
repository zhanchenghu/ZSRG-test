from time import sleep

import pytest

from common.driver_tool import DriverTool
from common.read_json_tool import ReadJSONTool
from config import TestConfig
from pages.web.tpshop.frontend.cart_page import CartPage
from pages.web.tpshop.frontend.home_page import TPShopHomePageWeb
from pages.web.tpshop.frontend.login_page import TPShopLoginPageWeb
from pages.web.tpshop.frontend.my_account_page import TPShopMyAccountPageWeb
from pages.web.tpshop.frontend.order_confirm_page import OrderConfirmPage
from pages.web.tpshop.frontend.order_pay_page import OrderPayPage
from pages.web.tpshop.frontend.pay_result_page import PayResultPage
from pages.web.tpshop.frontend.search_result_page import TPShopSearchResultPageWeb


@pytest.mark.run(order=2)
class TestTPShopFrontEnd(object):
    def setup_class(self):
        """
        打开浏览器
        :return:
        """
        self.driver = DriverTool.get_web_driver()

    def teardown_class(self):
        """
        所有的测试方法执行完成后执行， 关闭浏览器
        :return:
        """
        DriverTool.kill_web_driver()

    @pytest.mark.parametrize(argnames="user_name, password, verify_code, error_message, succeed, description",
                             argvalues=ReadJSONTool.read_json("web/front_end_user.json"))
    def test_tp_shop_login(self, user_name, password, verify_code, error_message, succeed, description):
        print(description)
        # 访问首页
        DriverTool.visit_url("http://hmshop-test.itheima.net/")
        # 点击登录
        # Page Object: 页面对象
        # TPShopHomePage() 首页的页面对象
        TPShopHomePageWeb().go_to_login_page()
        # 进入登录页面
        # 创建TPShopLoginPage() 登录页面的对象
        login_page = TPShopLoginPageWeb()
        login_page.login(user_name, password, verify_code)

        # 进入我的账号页面
        # 获取当前登录的账号名字
        if succeed:
            account = TPShopMyAccountPageWeb().get_my_account()
            # 断言结果
            assert user_name == account
        else:
            msg = login_page.get_login_error_message()
            assert msg == error_message

    def test_search_and_buy(self):
        # 访问首页
        DriverTool.visit_url("http://hmshop-test.itheima.net/")
        # 在首页搜索商品
        TPShopHomePageWeb().search_product("上海团长_" + TestConfig.get_random_str())

        # 在搜索结果页面，查找搜索到的商品
        search_page = TPShopSearchResultPageWeb()
        count = search_page.get_products_count()
        assert count > 0

        # 购买的过程

        # 添加购物车
        search_page.add_product_to_cart()
        # 跳转到购物车
        search_page.go_to_cart()

        # 购物车页面
        cart_page = CartPage()
        # 勾选全部商品
        cart_page.check_all_product()
        # 结算
        cart_page.go_to_pay()

        # # 跳转到了 订单确认页面
        order_confirm_page = OrderConfirmPage()
        # # 提交订单
        order_confirm_page.submit_order()

        # # 进入支付页面
        pay_page = OrderPayPage()
        # # 选择支付方式
        pay_page.select_pay_method()
        # # 确认支付
        pay_page.confirm()

        # # 支付结果页面
        pay_result_page = PayResultPage()
        # # 获取支付结果
        result = pay_result_page.get_result()
        # 验证交易成功
        assert result == "订单提交成功，我们将在第一时间给你发货！"
