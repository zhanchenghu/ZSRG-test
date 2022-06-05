from appium.webdriver.common.mobileby import MobileBy

from base.app_base_page import AppBasePage


class SearchResultPage(AppBasePage):
    def __init__(self):
        # 搜索框定位器
        self.search_box_locator = (MobileBy.ID, "com.tpshop.malls:id/search_et")
        # 搜索按钮定位器
        self.search_btn_locator = (MobileBy.ID, "com.tpshop.malls:id/search_btn")

        # 定位商品名称的定位器
        self.product_name_locator = (MobileBy.ID, "com.tpshop.malls:id/product_name_tv")

        # 定位商品图片
        self.product_img_locator = (MobileBy.ID, "com.tpshop.malls:id/product_pic_img")

    def search_product(self, product_name):
        """
        搜索上坪
        :param product_name: 商品名称
        :return:
        """
        # 输入要搜索的商品名称
        search_box = self.search_element(self.search_box_locator)
        self.input(search_box, product_name)

        # 点击搜索按钮
        self.search_element(self.search_btn_locator).click()

    def search_product_count(self):
        return len(self.search_elements(self.product_name_locator))

    def go_to_product_detail(self):
        self.search_element(self.product_img_locator).click()
