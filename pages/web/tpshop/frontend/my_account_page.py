from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class TPShopMyAccountPageWeb(WebBasePage):
    def __init__(self):
        # 账号名字定位器
        self.my_account_link_locator = (By.CLASS_NAME, "mu-m-phone")

    def get_my_account(self):
        """
        :return:获取当前登录的账号名
        """
        my_account_link = self.search_element(self.my_account_link_locator)
        return my_account_link.text
