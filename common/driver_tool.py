from selenium import webdriver as web
from appium import webdriver as app

from config import TestConfig


class DriverTool:
    # web自动化打开的浏览器对象
    __web_driver = None

    # app自动化打开的会话
    __app_driver = None

    # Web driver 相关方法
    @classmethod
    def get_web_driver(cls):
        if cls.__web_driver is None:
            cls.__web_driver = web.Chrome(TestConfig.get_file_path("chromedriver"))
            cls.__web_driver.maximize_window()
            # 不用隐式等待，改用显示等待
            # cls.__driver.implicitly_wait(30)
        return cls.__web_driver

    @classmethod
    def kill_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
        cls.__web_driver = None

    @classmethod
    def clear_web_cookie(cls):
        if cls.__web_driver:
            cls.__web_driver.delete_all_cookies()

    @classmethod
    def visit_url(cls, url):
        if url and cls.__web_driver:
            cls.__web_driver.get(url)

    # app driver相关的方法
    @classmethod
    def get_app_driver(cls, package, activity):
        """
        获取app driver
        :param package: 默认打开的应用包名
        :param activity: 默认打开的应用页面名
        :return: app driver 会话
        """
        if cls.__app_driver is None:
            cls.__app_driver = app.Remote("http://127.0.0.1:4723/wd/hub", {
                "platformName": "Android",  # 必须
                "platformVersion": "7.1",  # 必须。 只需要写前两个版本。 模拟器 《设置》-> 版本号
                "deviceName": "Android Emulater",  # appium server不用但是必须写
                "appPackage": package,
                "appActivity": activity,
                "unicodeKeyboard": True,
                "resetKeyboard": True
            })
        return cls.__app_driver

    @classmethod
    def get_app(cls):
        """
        获取到之前打开的会话
        :return:
        """
        return cls.__app_driver

    @classmethod
    def kill_app_driver(cls):
        if cls.__app_driver:
            cls.__app_driver.quit()
        cls.__app_driver = None

    @classmethod
    def start_activity(cls, package, activity):
        if package and activity and cls.__app_driver:
            cls.__app_driver.start_activity(package, activity)
