from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.web_base_page import WebBasePage
from common.driver_tool import DriverTool


class TPShopLoginPageWeb(WebBasePage):
    def __init__(self):
        # 使用ID定位用户名输入框
        # ID： username
        self.user_name_locator = (By.ID, "username")

        # 使用ID定位密码输入框
        # ID： password
        self.password_locator = (By.ID, "password")

        # 使用ID定位验证码输入框
        # ID: verify_code
        self.verify_code_locator = (By.ID, "verify_code")

        # 使用NAME定位登录按钮
        # NAME: sbtbutton
        self.login_btn_locator = (By.NAME, "sbtbutton")

        # 使用class定位： 错误信息
        # class: layui-layer-content
        self.error_message_locator = (By.CLASS_NAME, "layui-layer-content")

    def login(self, user_name, password, verify_code):
        # 调用父类的search_element 显示定位用户名输入框
        user_name_box = self.search_element(self.user_name_locator)
        # 调用父类的输入。 输入用户名
        self.input(user_name_box, user_name)

        # 使用显示等待查找密码输入框
        password_box = self.search_element(self.password_locator)
        # 输入密码
        self.input(password_box, password)

        # 同上
        verify_code_box = self.search_element(self.verify_code_locator)
        # 输入密码
        self.input(verify_code_box, verify_code)

        # 定位到登录按钮。
        # 点击
        # 使用显示等待，查找登录按钮
        login_btn = self.search_element(self.login_btn_locator)
        login_btn.click()

    def get_login_error_message(self):
        return self.search_element(self.error_message_locator).text
