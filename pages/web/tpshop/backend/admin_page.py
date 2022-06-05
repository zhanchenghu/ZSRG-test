from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.web_base_page import WebBasePage
from common.driver_tool import DriverTool


class AdminPage(WebBasePage):
    def __init__(self):
        # 用户名定位器
        self.user_name_locator = (By.CLASS_NAME, "bgdopa-t")

        # 首页定位器
        self.home_page_locator = (By.LINK_TEXT, "首页")

        # frame的定位器
        self.frame_locator = (By.ID, "workspace")

        # 定位“商品管理”链接
        self.product_manage_link_locator = (By.XPATH, '//*[@class="commfunc-con"]/a[1]')

        # 定位添加商品按钮
        self.add_product_link_locator = (By.XPATH, '//*[text()="添加商品"]')

        # 定位商品表单里面的元素

        # 1 定位实物商品链接
        self.product_type_locator = (By.CLASS_NAME, "curtab")

        # 2 商品名称定位器
        self.product_name_locator = (By.NAME, "goods_name")

        # 3 商品分类
        self.product_category_locator_1 = (By.ID, "cat_id")
        self.product_category_locator_2 = (By.ID, "cat_id_2")
        self.product_category_locator_3 = (By.ID, "cat_id_3")

        # 4 本店售价
        self.my_price_locator = (By.NAME, "shop_price")
        # 5 市场售价
        self.market_price_locator = (By.NAME, "market_price")

        # 6 定位“是”这个包邮按钮
        self.shipping_yes_locator = (By.ID, "is_free_shipping_label_1")

        # 7 定位“否”这个包邮按钮
        self.shipping_no_locator = (By.ID, "is_free_shipping_label_0")

        # 8 定位包邮模板
        self.shipping_method_locator = (By.NAME, "template_id")

        # 9 定位库存输入框
        self.store_count_locator = (By.NAME, "store_count")

        # 10 定位确认提交按钮
        self.submit_locator = (By.ID, "submit")

    def get_current_login_user(self):
        # 定位到用户名输入框
        user_name_span = self.search_element(self.user_name_locator)
        # 因为后台返回用户名时快、时慢。 此处加一个强制等待保证能拿到用户名信息
        sleep(2)

        return user_name_span.text

    def go_to_product_list(self):
        """
        跳转到商品列表子页面
        :return:
        """
        # 点击首页
        self.search_element(self.home_page_locator).click()
        frame_element = self.search_element(self.frame_locator)
        # 切到frame里面
        DriverTool.get_web_driver().switch_to.frame(frame_element)
        try:
            # 点击商品管理
            self.search_element(self.product_manage_link_locator).click()
        finally:
            # 切到主页面
            DriverTool.get_web_driver().switch_to.default_content()

    def go_to_create_product(self):
        """
        点击创建商品按钮
        :return:
        """
        frame_element = self.search_element(self.frame_locator)
        DriverTool.get_web_driver().switch_to.frame(frame_element)
        try:
            self.search_element(self.add_product_link_locator).click()
        finally:
            DriverTool.get_web_driver().switch_to.default_content()

    def save_product(self,
                     product_name,
                     category_1,
                     category_2,
                     category_3,
                     my_price,
                     market_price,
                     shipping,
                     shipping_method,
                     amount):
        """
        保存商品
        :param product_name: 商品名称
        :param category_1: 分类1
        :param category_2:分类2
        :param category_3:分类3
        :param my_price: 本店价格
        :param market_price:市场价格
        :param shipping: 是否包邮
        :param shipping_method: 选择包邮时的模板名称
        :param amount: 库存数量
        :return:
        """
        frame_element = self.search_element(self.frame_locator)
        DriverTool.get_web_driver().switch_to.frame(frame_element)

        try:
            # 点击商品类型： 实物
            self.search_element(self.product_type_locator).click()

            # 输入商品名称
            name_box = self.search_element(self.product_name_locator)
            self.input(name_box, product_name)

            # 选择三个分类
            c_1 = self.search_element(self.product_category_locator_1)
            Select(c_1).select_by_visible_text(category_1)

            sleep(1)
            c_2 = self.search_element(self.product_category_locator_2)
            Select(c_2).select_by_visible_text(category_2)

            sleep(1)
            c_3 = self.search_element(self.product_category_locator_3)
            Select(c_3).select_by_visible_text(category_3)

            # 输入市场价、本店价
            my_price_box = self.search_element(self.my_price_locator)
            self.input(my_price_box, my_price)

            market_price_box = self.search_element(self.market_price_locator)
            self.input(market_price_box, market_price)

            if shipping:
                # 点击包邮的“是”
                self.search_element(self.shipping_yes_locator).click()
            else:
                # 点击包邮的 “否”
                self.search_element(self.shipping_no_locator).click()

                # 选择包邮的模板
                shipping_method_select = self.search_element(self.shipping_method_locator)
                Select(shipping_method_select).select_by_visible_text(shipping_method)

            store_count_box = self.search_element(self.store_count_locator)
            self.input(store_count_box, amount)

            # 点击提按钮
            self.search_element(self.submit_locator).click()
        finally:
            DriverTool.get_web_driver().switch_to.default_content()

    def get_product_by_name(self, product_name):
        """
        使用商品名称， 从商品列表中获取商品
        :param product_name: 商品名称
        :return: 如果能找到， 返回一个商品名称。 如果找不到返回TimeoutException
        """
        frame_element = self.search_element(self.frame_locator)
        DriverTool.get_web_driver().switch_to.frame(frame_element)
        try:
            # 根据product name动态组装一个xpath语法
            locator = (By.XPATH, f'//*[text()="{product_name}"]')
            return self.search_element(locator).text
        finally:
            DriverTool.get_web_driver().switch_to.default_content()
