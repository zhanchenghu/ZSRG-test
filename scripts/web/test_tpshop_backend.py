import pytest

from common.driver_tool import DriverTool
from common.read_json_tool import ReadJSONTool
from config import TestConfig
from pages.web.tpshop.backend.admin_page import AdminPage
from pages.web.tpshop.backend.login_page import LoginPage


@pytest.mark.run(order=1)
class TestTPShopBackend(object):
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
                             argvalues=ReadJSONTool.read_json(r"web/backend.json"))
    def test_backend_login(self, user_name, password, verify_code, error_message, succeed, description):
        # 访问后台登录页面
        DriverTool.visit_url("http://hmshop-test.itheima.net/index.php/Admin/Admin/login")

        # 完成登录
        LoginPage().login(user_name, password, verify_code)

        # 获取当前登录的账号
        login_user = AdminPage().get_current_login_user()

        assert login_user == user_name

    @pytest.mark.parametrize(argnames="""product_name,
                                     category_1,
                                     category_2,
                                     category_3,
                                     my_price,
                                     market_price,
                                     shipping,
                                     shipping_method,
                                     amount""", argvalues=ReadJSONTool.read_json("web/product.json"))
    def test_backend_release_product(self,
                                     product_name,
                                     category_1,
                                     category_2,
                                     category_3,
                                     my_price,
                                     market_price,
                                     shipping,
                                     shipping_method,
                                     amount):
        # 访问后台页面: http://hmshop-test.itheima.net/index.php/Admin/Index/index
        DriverTool.visit_url("http://hmshop-test.itheima.net/index.php/Admin/Index/index")

        admin_page = AdminPage()

        # 跳转到商品列表
        admin_page.go_to_product_list()

        # 点击创建商品
        admin_page.go_to_create_product()

        # 保存商品
        new_product_name = product_name + TestConfig.get_random_str()
        admin_page.save_product(new_product_name,
                                category_1,
                                category_2,
                                category_3,
                                my_price,
                                market_price,
                                shipping,
                                shipping_method,
                                amount)
        # 根据商品名称获取商品
        name = admin_page.get_product_by_name(new_product_name)

        assert name == new_product_name
