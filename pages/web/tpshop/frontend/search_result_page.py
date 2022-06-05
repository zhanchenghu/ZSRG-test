from time import sleep

from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class TPShopSearchResultPageWeb(WebBasePage):
    def __init__(self):
        # 定位所有商品
        self.product_list_locator = (By.XPATH, '//*[@class="shop-list-splb p"]/ul/li')

        # 定位到第一个商品的 “添加购物车” 按钮
        self.add_cart_locator = (By.LINK_TEXT, "加入购物车")

        # 关闭按钮定位
        self.close_wd_locator = (By.CLASS_NAME, "layui-layer-close")

        # 定位到购物车按钮
        self.cart_btn_locator = (By.CLASS_NAME, "c-n")

    def get_products_count(self):
        # 返回商品列表的长度
        return len(self.search_elements(self.product_list_locator))

    def add_product_to_cart(self):
        # 点击添加购物车
        self.search_element(self.add_cart_locator).click()

        # 弹出框一直有，默认是是不显示的。 需要等弹出成功以后再点， 休2秒
        sleep(2)

        # 点击关闭窗口按钮
        self.search_element(self.close_wd_locator).click()

    def go_to_cart(self):
        self.search_element(self.cart_btn_locator).click()
