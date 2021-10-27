import time
import unittest
import os
from browser.browser import CHROME
from util.decorector import log


class YdyBaseTestCase(unittest.TestCase):
    """
    用于所有TestCase的基类，此类仅用于继承和代码调试，正常用例执行在executor里执行子类文件

    """

    ul = None

    @classmethod
    def setUpClass(cls):
        print("开始执行用例")

    @classmethod
    def tearDownClass(cls):

        print("用例执行完毕")

    def setUp(self):
        # 获取driver，chrome里面不指定位置是因为提前在环境变量里面配置了driver。
        self.driver = CHROME().browser
        # 最大化浏览器窗口，也可以不写这个，在chrome增加启动参数
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(2)
        # 每条用例如果报错，就会直接进入teardown，正常结束也会进入这里。
        for method, error in self._outcome.errors:
            # 如果发生任何错误，我们接在这里进行截图处理
            if error:
                # 获取错误用例方法名字
                case_name = self._testMethodName
                dir_path = os.path.join(os.path.dirname(os.getcwd()), 'error_image')
                # 图片存储位置
                image_name = dir_path + "\\" + case_name + ".png"
                # 截图操作
                self.driver.save_screenshot(image_name)
        self.driver.close()

    # @unittest.skipIf()
    # @unittest.skipUnless()
    # @unittest.skip
    # @unittest.expectedFailure()
    def test_ydy_test(self):
        pass
