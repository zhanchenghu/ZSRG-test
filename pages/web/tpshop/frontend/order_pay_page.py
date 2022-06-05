from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class OrderPayPage(WebBasePage):
    def __init__(self):
        # 确认提交按钮的定位器
        self.confirm_pay_btn_locator = (By.CLASS_NAME, "button-confirm-payment")

    def select_pay_method(self, pay_method="余额"):
        """
        选择支付方式
        :param pay_method: 支付方式。从 余额、财付通、银联、微信、支付宝 中选一个
        :return: 无
        """
        methods = {
            "余额": "pay_code=cod",
            "财付通": "pay_code=tenpay",
            "银联": "pay_code=unionpay",
            "微信": "pay_code=weixin",
            "支付宝": "pay_code=newalipay"
        }
        value = methods.get(pay_method)
        if value is None:
            raise Exception("pay_method 参数必须是: 余额、财付通、银联、微信、支付宝 中的一个！")

        locator = (By.XPATH, f'//*[@value="{value}"]')
        self.search_element(locator).click()

    def confirm(self):
        """
        确认提交
        :return:
        """
        self.search_element(self.confirm_pay_btn_locator).click()
