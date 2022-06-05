from selenium.webdriver.common.by import By

from base.web_base_page import WebBasePage


class PayResultPage(WebBasePage):
    def __init__(self):
        self.result_locator = (By.XPATH, '//*[@class="erhuh"]/h3')

    def get_result(self):
        """
        获取提交订单后的结果
        :return:
        """
        return self.search_element(self.result_locator).text
