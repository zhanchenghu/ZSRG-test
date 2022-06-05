from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class TPShopHomePageWeb(WebBasePage):

    def __init__(self):
        self.login_btn_locator = (By.LINK_TEXT, "登录")
        # 定位搜索框
        # ID： q
        self.search_box_locator = (By.ID, "q")

        # 定位搜索按钮
        # Class： ecsc-search-button
        self.search_btn_locator = (By.CLASS_NAME, "ecsc-search-button")

    def go_to_login_page(self):
        self.search_element(self.login_btn_locator).click()

    def search_product(self, product_name):
        # 定位到搜索框， 输入 product_name
        product_name_box = self.search_element(self.search_box_locator)
        self.input(product_name_box,product_name)
        # 定位搜索按钮，点击搜索
        self.search_element(self.search_btn_locator).click()
