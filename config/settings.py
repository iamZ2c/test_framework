# -*- coding: utf-8 -*-
import os
import platform

# ------------------------------BROWSER_SETTINGS--------------------------------------------

# 隐式等待时间


IMP_TIME = 30
# 页面加载时间
PAGE_LOAD_TIME = 20
# js加载时间
SCRIPT_TIME_OUT = 20

HEADLESS = False

IE_DRIVER_PATH = ''

# ------------------------------CHROME_SETTINGS----------------------------------------------
START_MAX = True
CHROME_DRIVER_PATH = None
if platform.system() == 'Windows':
    CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.getcwd()), 'driver', 'chromedriver.exe')

elif platform.system() == 'Linux':
    CHROME_DRIVER_PATH = os.path.join(os.path.dirname(os.getcwd()), 'driver', 'chromedriver')

print(CHROME_DRIVER_PATH)
# 是否提添加启动参数
CHROME_OPTION_MARK = True
# 启动完成后的操作
CHROME_METHOD_MARK = True

CHROME_HEADLESS = True

CHROME_IMP_TIME = 30

CHROME_PAGE_LOAD_TIME = 30

CHROME_SCRIPT_TIME_OUT = 30

CHROME_WINDOW_SIZE = (1920, 900)

ARGS = []

if HEADLESS:
    ARGS.append('--headless')
else:
    ...
if START_MAX:
    if platform.system() == 'Windows':
        ARGS.append('--start-maximized')
    elif platform.system() == 'Linux':
        ARGS.append('--kiosk')

EXP = {
    # 不显示chrome浏览器正在收到自动化浏览软件的控制
    'excludeSwitches': ['enable-automation'],
    # 以iphone6的分辨打开网站
    # 'mobileEmulation': {'deviceName': 'iPhone 6'},

    'args': ARGS,
    'prefs': {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False
    }
}


CHROME_CAPS = {
    'capabilities': {
        'firstMatch:': [{}],
        'alwaysMatch': {
            'browserName': 'chrome',
            'platformName': 'any',
            "timeouts": {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            },
            'goog:chromeOptions': EXP
        }
    }
}

# ------------------------------PROJECT_SETTINGS----------------------------------------------
PROJECT_URL = "https://www.baidu.com/"

BY_RULES = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

# ------------------------------SMTP_EMAIL_SETTINGS--------------------------------------------


SENDER = 'iam2cc@foxmail.com'

RECEIVERS = ['1059995908@qq.com', ]

SERVER = "smtp.qq.com"

AUTH_CODE = 'oqmnkweutuugbbcj',

TITLE = "TEST-REPORT"
# 邮件正文
MESSAGE = None
# 附件
ATTACHMENT_FILE = None

# ------------------------------CASE_EXECUTOR_SETTINGS--------------------------------------
GENERATE_TEST_REPORT = False

REPORT_NAME = "质保部自动化测试报告"

REPORT_TITLE = 'TestReport'

SEND_EMAIL = False

RECEIVERS_EMAIL = "1059995908@qq.com"

# ------------------------------READER_SETTINGS--------------------------------------
EXCEL_FILE_PATH = os.path.join(os.path.dirname(os.getcwd()), 'config', 'tips_and_text.xls')

ELEMENT_LOCATE_FILE_PATH = os.path.join(os.path.dirname(os.getcwd()), "config", "LocateElement.ini")

DATA_BASE_FILE_PATH = os.path.join(os.path.dirname(os.getcwd()), "db_servers", "database.ini")
