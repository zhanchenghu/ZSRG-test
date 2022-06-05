from time import sleep

from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class CartPage(WebBasePage):

    def __init__(self):
        # 用来判断是否选中的 全选按钮定位器
        self.check_all_btn_locator = (By.XPATH, '//*[@class="column cart-checkbox"]/input')

        # 被点击的 全选按钮定位器
        self.check_all_btn_locator_2 = (By.CLASS_NAME, "checkFull")

        # 去结算按钮定位器
        self.go_to_pay_btn_locator = (By.CLASS_NAME, "paytotal")

    def check_all_product(self):
        """
        选中购物车所有商品
        1. 检查是否已经全部选中
        2. 如果没有全选中。 就去选中全部
        3. 如果已经全选了。 跳过
        :return:
        """
        check_box = self.search_element(self.check_all_btn_locator)
        if check_box.is_selected():
            return

        chk = self.search_element(self.check_all_btn_locator_2)
        sleep(3)
        chk.click()

    def go_to_pay(self):
        """
        去结算
        :return:
        """
        self.search_element(self.go_to_pay_btn_locator).click()
