from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class HomePage(AppBasePage):
    def __init__(self):
        # 底部我的头像
        self.my_locator = (MobileBy.ID, "com.tpshop.malls:id/mine_img")
        # 我的首页上面的用户头像
        self.my_photo_locator = (MobileBy.ID, "com.tpshop.malls:id/head_img")
        # 登陆完成后的用户名
        self.my_name_locator = (MobileBy.ID, "com.tpshop.malls:id/nick_name_tv")

        # 首页定位器
        self.home_locator = (MobileBy.ID, "com.tpshop.malls:id/home_img")

        # 顶部搜索框的定位器
        self.search_box_locator = (MobileBy.XPATH, "//*[@text='输入你想要搜索的内容']")

    def go_to_login(self):
        # 定位到 ”我的“， 并点击
        self.search_element(self.my_locator).click()
        # 定位到 ”头像“， 并点击
        self.search_element(self.my_photo_locator).click()

    def go_to_home(self):
        """
        返回首页
        :return:
        """
        self.search_element(self.home_locator).click()

    def go_to_search(self):
        """
        点击顶部搜索框
        :return:
        """
        self.search_element(self.search_box_locator).click()

    def get_current_user_name(self):
        """
        获取当前登录的账号名称
        :return:
        """
        return self.search_element(self.my_name_locator).text
