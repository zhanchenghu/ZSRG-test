import os
from datetime import datetime


class TestConfig:
    __rand_str = None

    @staticmethod
    def get_file_path(file_name):
        """
        获取文件的绝对目录
        :param file_name: 要找的文件， 注意只提供文件名即可不需要 /
        :return: 文件的绝对地址
        """
        return os.path.dirname(__file__) + "/" + file_name

    @classmethod
    def get_random_str(cls):
        if cls.__rand_str is None:
            cls.__rand_str = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return cls.__rand_str