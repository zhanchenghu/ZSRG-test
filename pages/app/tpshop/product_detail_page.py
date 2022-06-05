from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class ProductDetailPage(AppBasePage):
    def __init__(self):
        # 定位购买按钮
        self.buy_btn_locator = (MobileBy.ID, "com.tpshop.malls:id/promptly_buy_tv")
        # 确定购买按钮
        self.confirm_btn_locator = (MobileBy.ID, "com.tpshop.malls:id/confirm_tv")

    def buy(self):
        # 点击购买
        self.search_element(self.buy_btn_locator).click()
        # 点击确认
        self.search_element(self.confirm_btn_locator).click()
