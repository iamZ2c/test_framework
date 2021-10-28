import configparser
import os


class IniReader:
    def __init__(self, file_path=None):
        self._data = {}
        if file_path is None:
            self.file_path = os.path.join(os.path.dirname(os.getcwd()), "config", "LocateElement.ini")
        self.config = configparser.ConfigParser()
        self.config.read(file_path, encoding='utf-8')

    def get_config(self):
        return self.config

    def get_value(self, node, key):
        """
        获取配置文件里面的xpath
        :param key: xpath
        :param node: 节点位置
        :return:
        """
        try:
            element_info = self.config.get(node, key)
            return element_info
        except configparser.NoOptionError:
            print("<未找到node:{}，key:{}的信息,请检查配置文件>".format(node, key))

    def data(self, node):
        if not self._data:
            for k, v in self.config.items(node):
                self._data[k] = int(v) if k in ('port', 'maxsize', 'minsize', 'max', 'min', 'increment') else v
        return self._data

# 测试模块代码
# r1 = IniReader(file_path='/Users/bytedance/Desktop/test_framework/db_servers/database.ini')
# print(r1.data('MYSQL'))
# print(r1.get_value(node="MYSQL", key="port"))
# print(type(r1.get_value(node="RegisterElement", key="register_butto")))
