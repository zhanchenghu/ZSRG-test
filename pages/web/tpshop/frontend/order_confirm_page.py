from time import sleep

from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage
from common.driver_tool import DriverTool


class OrderConfirmPage(WebBasePage):
    def __init__(self):
        self.submit_btn_locator = (By.ID, "submit_order")

    def submit_order(self):
        """
        提交订单
        :return:
        """
        sleep(2)
        # 获取警告框
        alert_wd = DriverTool.get_web_driver().switch_to.alert
        # 点击确认
        alert_wd.accept()

        self.search_element(self.submit_btn_locator).click()
