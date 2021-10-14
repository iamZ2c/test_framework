from selenium.webdriver import *
from typing import Type, Union


# 异常类,检查输入的浏览器类型异常和选项异常
class BrowserException(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f'unsupported browser type: {self._type}'


# 基类整个类名大写是为了不与selenium包里面重名，导致奇怪的错误
class BROWSER:
    # 驱动路径
    CHROME_DRIVER_PATH = '/Users/bytedance/Desktop/test_framework/driver/chromedriver'

    # CHROME_DRIVER_PATH = 'C:\\Users\\iam2cc\\Desktop\\selfProject\\test_framework\\driver\\chromedriver.exe'
    IE_DRIVER_PATH = ''

    # WINDOW_SIZE = (1024, 768)
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
        # print("被调用")

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


class CHROME(BROWSER):
    # 是否提添加启动参数
    OPTION_MARK = True
    # 启动完成后的操作
    METHOD_MARK = True

    HEADLESS = False

    IMP_TIME = 30

    PAGE_LOAD_TIME = 30

    SCRIPT_TIME_OUT = 30

    WINDOW_SIZE = (1920, 900)

    START_MAX = "--kiosk"
    # mac "--kiosk"
    # windows '--start-maximized'

    EXP = {
        # 不显示chrome浏览器正在收到自动化浏览软件的控制
        'excludeSwitches': ['enable-automation'],
        # 以iphone6的分辨打开网站
        # 'mobileEmulation': {'deviceName': 'iPhone 6'}
    }

    @property
    def options(self):
        if self.OPTION_MARK:
            chrome_options = self._options()
            chrome_options.add_argument(self.START_MAX)

            for k, v in self.EXP.items():
                # 添加实验性质参数
                chrome_options.add_experimental_option(k, v)

            chrome_options.headless = self.HEADLESS
            return chrome_options
        else:
            return None

    @property
    def browser(self):
        """

        :return: 返回chrome_driver对象
        """
        # print("driver路径：", self._path)
        if self.options:
            print("driver路径：", self._path)
            chrome_browser = self._browser(
                self._path,
                options=self.options)
            print(chrome_browser)

        else:
            chrome_browser = self._browser(
                self._path,
            )
        if self.METHOD_MARK:
            chrome_browser.implicitly_wait(self.IMP_TIME)
            chrome_browser.set_script_timeout(self.SCRIPT_TIME_OUT)
            chrome_browser.set_window_size(*self.WINDOW_SIZE)
        return chrome_browser


class IE(BROWSER):
    CLEAN_SESSION = True

    def __init__(self):
        super(IE, self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path=super().IE_DRIVER_PATH
        )

    @property
    def options(self):
        ie_option = self._options()
        ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        ie_browser = self._browser(
            self.IE_DRIVER_PATH,
            options=self.options)
        ie_browser.set_page_load_timeout(self.PAGE_LOAD_TIME)
        ie_browser.implicitly_wait(self.IMP_TIME)
        ie_browser.set_script_timeout(self.SCRIPT_TIME_OUT)
        ie_browser.maximize_window()
        return ie_browser



# CHROME().browser.get(url='http://www.douxuedu.com/#/main/course')
