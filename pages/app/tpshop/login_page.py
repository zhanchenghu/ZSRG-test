from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class LoginPage(AppBasePage):
    def __init__(self):
        self.user_name_locator =(MobileBy.ID, "com.tpshop.malls:id/mobile_et")
        self.password_locator =(MobileBy.ID, "com.tpshop.malls:id/pwd_et")
        self.accept_btn_locator =(MobileBy.ID, "com.tpshop.malls:id/agree_btn")
        self.login_btn_locator = (MobileBy.ID, "com.tpshop.malls:id/login_tv")

    def login(self, user_name, password):
        # 定位到用户名输入框。 输入user_name
        # 定位到密码输入框。 输入password
        # 定位到 ”同意“， 点击
        # 定位到登录。 点击
        user_name_box = self.search_element(self.user_name_locator)
        self.input(user_name_box, user_name)

        password_box = self.search_element(self.password_locator)
        self.input(password_box, password)

        self.search_element(self.accept_btn_locator).click()

        self.search_element(self.login_btn_locator).click()
