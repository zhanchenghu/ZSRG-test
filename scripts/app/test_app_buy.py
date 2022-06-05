import pytest

from common.driver_tool import DriverTool
from config import TestConfig
from pages.app.tpshop.home_page import HomePage
from pages.app.tpshop.login_page import LoginPage
from pages.app.tpshop.order_page import OrderPage
from pages.app.tpshop.pay_page import PayOrderPage
from pages.app.tpshop.pay_result_page import PayResultPage
from pages.app.tpshop.product_detail_page import ProductDetailPage
from pages.app.tpshop.search_result_page import SearchResultPage


@pytest.mark.run(order=3)
class TestSettingSearch:

    def setup_class(self):
        """
        所有的测试方法执行之前执行， 打开会话
        使用下面指令获取包名、页面名
        adb shell dumpsys window windows | findstr mFocusedApp
        :return:
        """
        self.driver = DriverTool.get_app_driver("com.tpshop.malls", ".SPMainActivity")

    def teardown_class(self):
        """
        所有的测试方法执行完成后执行， 关闭浏览器
        :return:
        """
        DriverTool.kill_app_driver()

    def test_login(self):
        # 首页
        home_page = HomePage()

        # 点击”我的“
        # 点击 ”头像“
        home_page.go_to_login()

        # 进入登陆页面
        login_page = LoginPage()
        login_page.login("18621276983", "123456")

        user_name = home_page.get_current_user_name()
        assert user_name == "18621276983"

    def test_search_and_buy(self):
        home_page = HomePage()

        # 点击回到首页
        home_page.go_to_home()

        # 点一下搜索框
        home_page.go_to_search()

        # 到了搜索结果页面
        result_page = SearchResultPage()
        # 搜索商品
        result_page.search_product("上海团长_" + TestConfig.get_random_str())

        # 断言， 搜索出来一个商品
        count = result_page.search_product_count()
        assert count == 1

        # 点击去商品详情
        result_page.go_to_product_detail()

        #  商品详情页
        product_detail_page = ProductDetailPage()
        product_detail_page.buy()

        # 订单页面
        order_page = OrderPage()
        order_page.submit()

        # 支付页面
        pay_page = PayOrderPage()
        pay_page.select_pay_method()
        pay_page.confirm("123456")

        # 购买结果
        result_page = PayResultPage()
        result = result_page.get_result()

        assert result == "确认订单成功"
