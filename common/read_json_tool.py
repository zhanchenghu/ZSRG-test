import json

from config import TestConfig


class ReadJSONTool(object):
    @staticmethod
    def read_json(file_name):
        """
        根据传入的json文件，返回列表数据
        :param file_name: 要读取的文件名
        :return:[(),()]
        """
        result = []

        if file_name is None:
            return result

        file_path = TestConfig.get_file_path(fr"data/{file_name}")
        with open(file_path, encoding="UTF-8") as reader:
            for item in json.load(reader):
                result.append(tuple(item.values()))

        return result