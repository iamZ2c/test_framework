# -*- coding:utf-8 -*-
import unittest
# 参数化
from time import sleep

import paramunittest

from bussines.common.common_login_page import CommonLogin


@paramunittest.parametrized(
    ('yfadmin', '123456abc'),
    ('zhangchent', '123456abc'),
    ('zhangchentb', '123456abc'),
)
class TestLogin(unittest.TestCase, CommonLogin):

    # 固定方法名称
    def setParameters(self, name, password):
        self.name = name
        self.passport = password

    def test_login_success(self):
        self.get_page()
        self.driver.maximize_window()
        print(self.name, self.passport)
        self.login(self.name, self.passport)
        if self.element(*self.assert_element).text == '管理后台':
            print("校验通过")
        sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
