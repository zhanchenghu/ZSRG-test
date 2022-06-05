from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class LoginPage(WebBasePage):
    def __init__(self):
        # locator 定位器定位页面元素
        # 分别定位：用户名、密码、验证码输入框
        self.user_name_locator = (By.NAME, "username")
        self.password_locator = (By.NAME, "password")
        self.verify_code_locator = (By.ID, "vertify")

        # 登录按钮的定位器
        self.login_btn_locator = (By.NAME, "submit")

    def login(self, user_name, password, code):
        # 用户名的输入
        user_name_box = self.search_element(self.user_name_locator)
        self.input(user_name_box, user_name)

        # 密码输入
        password_box = self.search_element(self.password_locator)
        self.input(password_box, password)

        # 验证码输入
        verify_code_box = self.search_element(self.verify_code_locator)
        self.input(verify_code_box, code)

        # 点击登录
        login_btn = self.search_element(self.login_btn_locator)
        login_btn.click()
