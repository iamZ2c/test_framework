# -*- coding: utf-8 -*-
# ------------------------------CASE_EXECUTOR_SETTINGS--------------------------------------
GENERATE_TEST_REPORT = False

REPORT_NAME = "质保部自动化测试报告"

REPORT_TITLE = 'DouXueBaseLineTestReport'

SEND_EMAIL = True

RECEIVERS_EMAIL = "1059995908@qq.com"

# ------------------------------BROWSER_SETTINGS--------------------------------------------

# 隐式等待时间
IMP_TIME = 30
# 页面加载时间
PAGE_LOAD_TIME = 20
# js加载时间
SCRIPT_TIME_OUT = 20

HEADLESS = False

# CHROME_DRIVER_PATH = 'C:\\Users\\iam2cc\\Desktop\\selfProject\\test_framework\\driver\\chromedriver.exe'
IE_DRIVER_PATH = ''

# ------------------------------CHROME_SETTINGS----------------------------------------------
CHROME_DRIVER_PATH = 'C:\\Users\\iam2cc\\Desktop\\selfProject\\unitest_framework\\dirver\\chromedriver.exe'

# 是否提添加启动参数
CHROME_OPTION_MARK = True
# 启动完成后的操作
CHROME_METHOD_MARK = True

CHROME_HEADLESS = True

CHROME_IMP_TIME = 30

CHROME_PAGE_LOAD_TIME = 30

CHROME_SCRIPT_TIME_OUT = 30

CHROME_WINDOW_SIZE = (1920, 900)

START_MAX = "--kiosk"

EXP = {
    # 不显示chrome浏览器正在收到自动化浏览软件的控制
    'excludeSwitches': ['enable-automation'],
    # 以iphone6的分辨打开网站
    # 'mobileEmulation': {'deviceName': 'iPhone 6'}
}

# ------------------------------PROJECT_SETTINGS----------------------------------------------
PROJECT_URL = "http://www.zhixuetong.com.cn/"

BY_RULES = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]
