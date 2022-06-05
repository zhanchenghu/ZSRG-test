from selenium.webdriver.support.wait import WebDriverWait

from common.driver_tool import DriverTool


class AppBasePage(object):
    def search_element(self, locator, timeout=30, poll_frequency=0.1):
        """
        显示查找元素
        :param locator: 元组，用来查找元素
        :param timeout: 查找元素的超时时间，可以不传。默认 30秒
        :param poll_frequency: 查找元素的频率。 可以不川。 默认0.1
        :return: 要查找的元素
        """
        return WebDriverWait(DriverTool.get_app(), timeout, poll_frequency).until(
            lambda x: x.find_element(*locator))

    def search_elements(self, locator, timeout=30, poll_frequency=0.1):
        return WebDriverWait(DriverTool.get_app(), timeout, poll_frequency).until(
            lambda x: x.find_elements(*locator))

    def input(self, element, txt):
        """
        给输入框输入内容
        :param element: 输入框
        :param txt: 输入的文本
        :return: 没有
        """
        element.clear()
        element.send_keys(txt)
