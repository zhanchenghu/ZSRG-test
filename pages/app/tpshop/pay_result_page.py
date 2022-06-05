from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class PayResultPage(AppBasePage):
    def __init__(self):
        # 提交结果定位器
        self.pay_result_locator = (MobileBy.ID, "com.tpshop.malls:id/title_tv")

    def get_result(self):
        #定位到结果并返回文本内容
        return self.search_element(self.pay_result_locator).text
