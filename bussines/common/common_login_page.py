from browser.browser import CHROME
from page.base_page import Page


class CommonLogin(Page):
    # CHROME.OPTION_MARK = False
    driver = CHROME().browser
    url = "http://www.douxuedu.com/#/main/course"

    # 页面元素
    loginBt = ('xpath', '//*[@id="frame_box"]/header/header/div/span/span[3]')

    def get_page(self):
        self.driver.get(url=self.url)

    def login(self):
        self.element(*self.loginBt).click()


c = CommonLogin()
c.get_page()
# c.driver.maximize_window()
c.login()
