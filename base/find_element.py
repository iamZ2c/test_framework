from util.ini_reader import IniReader
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import CHROME
from config import settings


class FindElement:
    def __init__(self, driver=None, node=None):
        self.node = node
        if driver:
            self.driver = driver
        else:
            self.driver = CHROME.browser

    def get_element(self, key, node=None):
        """
        获取元素对象，未定到的时候，返回None
        :param node: node name
        :param key: key name
        :return: return element or None
        """
        if not node:
            node = self.node

        read_ini = IniReader()
        data = read_ini.get_value(node=node, key=key)
        by = data.split(">")[0]
        expression = data.split(">")[1]
        if by not in settings.BY_RULES:
            raise Exception(
                f'无法识别的方法:{data}'
            )
        else:
            element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((by, expression)))
            return element


# 测试代码
# d = webdr
# fd = FindElement(d)
# element = fd.get_element(node="RegisterElement", key="register_button")