from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class PayOrderPage(AppBasePage):
    def __init__(self):
        # 立即支付定位器
        self.pay_now_locator = (MobileBy.ID, "com.tpshop.malls:id/pay_btn")
        # 密码框定位器
        self.password_locator = (MobileBy.ID, "com.tpshop.malls:id/pwd_et")
        # 确认密码按钮定位器
        self.confirm_password_locator = (MobileBy.ID, "com.tpshop.malls:id/sure_tv")

    def select_pay_method(self, method="余额"):
        # com.tpshop.malls:id/balance_check  余额支付
        # com.tpshop.malls:id/unionpay_check  银联支付
        # com.tpshop.malls:id/alipay_check 支付宝支付
        # com.tpshop.malls:id/weixin_check 微信支付

        methods = {
            "余额": "com.tpshop.malls:id/balance_check",
            "银联": "com.tpshop.malls:id/unionpay_check",
            "支付宝": "com.tpshop.malls:id/alipay_check",
            "微信": "com.tpshop.malls:id/weixin_check"
        }
        id = methods.get(method)

        if id is None:
            raise Exception("pay_method 必须属于 余额、银联、支付宝、微信 中的一个")
        locator = (MobileBy.ID, id)

        self.search_element(locator).click()

    def confirm(self, password):
        # 确认支付
        self.search_element(self.pay_now_locator).click()
        # 输入支付密码
        password_box = self.search_element(self.password_locator)
        self.input(password_box, password)

        # 点击确认支付
        self.search_element(self.confirm_password_locator).click()
