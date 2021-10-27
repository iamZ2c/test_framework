import os
import unittest
from test_case import data_driven_test_case
# pip install html_testRunner
import HtmlTestRunner
from base import smtp_servers
from config.settings import *


# 此文件用于执行部分用例和控制执行顺序


class CaseExecutor:
    """
    case的执行类
    """

    def __init__(self, report=GENERATE_TEST_REPORT):
        """
        :param report:report为False的时候不会生成测试报告
        """
        self.ss = smtp_servers.SmtpServers()
        self.suite = unittest.TestSuite()
        self.case_path = os.path.join(os.path.dirname(os.getcwd()), 'test_case')
        self.report_path = os.path.join(os.path.dirname(os.getcwd()), 'report', '')
        # 管理时候生成报告
        if report is False:
            self.runner = unittest.TextTestRunner()
        else:
            self.runner = HtmlTestRunner.HTMLTestRunner(output=self.report_path,
                                                        report_name=REPORT_NAME,
                                                        descriptions=False,
                                                        report_title=REPORT_TITLE,
                                                        verbosity=3,
                                                        )

    def auto_send_email(self, file_names):
        if file_names:
            # TODO 这个地方传入的filename应该改为report的name，找地方去htmltestrunner里面去获取名称
            self.ss.sendmail(files_names=[file_names], receivers=RECEIVERS_EMAIL,
                             e_text="测试代码")
        else:
            r = self.ss.get_all_report()
            self.ss.sendmail(files_names=r, receivers="929236578@qq.com", e_text="测试代码")

    def execute_testcaseydy(self, email=False, file_name=None):
        """
        :param email:默认False,True将发送邮件
        :param file_name:默认为空,将发送report目录下面所有的report,给出名字只发送一个.必须穿入list
        :return:None
        """
        # 加载部分执行的用例,使用ddt数据驱动的时候,会改变方法名称导致用例无法顺利加载进容器,需要重新按照此类型重写方法名。
        # old:test_tip_text
        # par:"phone_num_None_tip", "请输入手机号"
        # new:test_tip_text_1___phone_num_None_tip____请输入手机号__
        # 数字为索引序号
        self.suite.addTest(data_driven_test_case.DataDrivenTestCase('test_tip_text_1___phone_num_None_tip____请输入手机号__'))
        self.runner.run(self.suite)
        if email is True:
            self.auto_send_email(file_name)

    def run_all_case(self, email=SEND_EMAIL, file_name=None):
        # 默认执行所有用例
        if file_name:
            suite = unittest.defaultTestLoader.discover(self.case_path, file_name)
            self.runner.run(suite)
        else:
            suite = unittest.defaultTestLoader.discover(self.case_path, '*case.py')
            self.runner.run(suite)
        if email is True:
            self.auto_send_email(file_name)


if __name__ == '__main__':
    ce = CaseExecutor()
    ce.run_all_case()
