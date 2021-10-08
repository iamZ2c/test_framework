from selenium.webdriver import *
from typing import Type, Union


# 异常类
class BrowserException(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'unsupported browser type: {self._type}'


# 基类
class Browser:
    CHROME_DRIVER_PATH = './driver/chromedriver'

    WINDOW_SIZE = (1024, 768)
    # 隐式等待时间
    IMP_TIME = 30
    # 页面加载时间
    PAGE_LOAD_TIME = 20
    # js加载时间
    SCRIPT_TIME_OUT = 20

    HEADLESS = True

    def __init__(self,
                 browser_type: Type[Union[Firefox, Chrome, Ie, Safari]] = Chrome,

                 option_type: Type[Union[FirefoxOptions, ChromeOptions, IeOptions]] = ChromeOptions,

                 driver_path: str = CHROME_DRIVER_PATH
                 ):
        # 检查入参是否正常
        if not issubclass(browser_type, (Firefox, Chrome, Ie, Safari)):
            raise BrowserException(browser_type)

        if not issubclass(option_type, (FirefoxOptions, ChromeOptions, IeOptions)):
            raise BrowserException(option_type)

        if not isinstance(driver_path, str):
            raise TypeError
        self._path = driver_path
        self._browser = browser_type
        self._options = option_type

    @property
    def options(self):
        """
        浏览器特定操作
        :return:
        """
        return

    @property
    def browser(self):
        """
        启动浏览器并且返回实例对象
        :return:
        """
        return


class Chrome(Browser):
    HEADLESS = False

    IMP_TIME = 30

    PAGE_LOAD_TIME = 30

    SCRIPT_TIME_OUT = 30

    WINDOW_SIZE = (1920, 900)

    START_MAX = '--start-maximized'

    EXP = {
        # 不显示chrome浏览器正在收到自动化浏览软件的控制
        'excludeSwitches': ['enable-automation'],
        # 以iphone6的分辨打开网站
        'mobileEmulation': {'devicesName': 'iPhone6'}
    }

    @property
    def options(self):
        chrome_options = self._options()
        chrome_options.add_argument(self.START_MAX)

        for k, v in self.EXP:
            chrome_options.add_experimental_option(k, v)

        chrome_options.headless = self.HEADLESS
        return chrome_options


