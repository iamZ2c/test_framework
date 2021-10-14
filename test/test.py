# -*- coding:utf-8 -*-
import unittest
# 参数化
import paramunittest
from time import sleep
from bussines.common.common_login_page import CommonLogin

# 第三方包做参数化，需要在给出类装饰器和实现setParameters方法
# @paramunittest.parametrized(
#     ('yfadmin', '123456abc'),
#     ('zhangchent', '123456abc'),
#     ('zhangchentb', '123456abc'),
# )
# class TestLogin(unittest.TestCase, CommonLogin):
#
#     # 固定方法名称
#     def setParameters(self, name, password):
#         self.name = name
#         self.passport = password
#
#     def test_login_success(self):
#         self.get_page()
#         self.driver.maximize_window()
#         print(self.name, self.passport)
#         self.login(self.name, self.passport)
#         if self.element(*self.assert_element).text == '管理后台':
#             print("校验通过")
#         sleep(2)
#         self.driver.close()


# unittest原生方法TestCase类的subTest()实例方法,看上去好像是普通的循环，但是遇到assert false之后还是可以继续执行,
# subText方式写出的
# subText 方法里面的item必须是字典可格式的和上一个方法有所区别
data = (
    {"account": 'yfadmin', 'pwd': "123456abc"},
    {"account": 'zhangchent', 'pwd': "123456abc"},
    {"account": 'zhangchentb', 'pwd': "123456abc"},
)


class TestLogin2(unittest.TestCase, CommonLogin):
    def setUp(self) -> None:
        self.get_page()

    def test_login_success(self):
        for d in data:
            with self.subTest(d):
                self.login(d['account'], d['pwd'])
                try:
                    # assert 关键字，前面给了表达式后，后面可补充其他函数来运用 false的结果。
                    assert self.element(*self.assert_element).text == '管理后台', \
                        self.driver.save_screenshot(f'../err_img/{d["account"]}.png')
                finally:
                    sleep(2)
                    self.log_out()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
