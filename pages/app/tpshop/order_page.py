from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class OrderPage(AppBasePage):
    def __init__(self):
        # 确认提交订单按钮
        self.submit_order_btn_locator = (MobileBy.ID, "com.tpshop.malls:id/submit_tv")

    def submit(self):
        # 点击提交订单
        self.search_element(self.submit_order_btn_locator).click()
