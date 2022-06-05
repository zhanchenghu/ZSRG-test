from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class HomePage(AppBasePage):
    def __init__(self):
        # 定位器
        # 定位放大镜元素的locator
        self.search_btn_locator = (MobileBy.ID, "com.android.settings:id/search")

        # 定位输入框的locator
        self.search_box_locator = (MobileBy.ID, "android:id/search_src_text")

    def search_text(self, text):
        """
        设置中查找文本
        :param text: 查找的内容
        :return:
        """
        #定位到放大镜，点击
        search_btn = self.search_element(self.search_btn_locator)
        search_btn.click()

        search_box = self.search_element(self.search_box_locator)
        self.input(search_box,text)






