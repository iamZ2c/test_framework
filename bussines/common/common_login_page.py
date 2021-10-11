from time import sleep

from browser.browser import CHROME
from page.base_page import Page


class CommonLogin(Page):
    # CHROME.OPTION_MARK = False
    driver = CHROME().browser
    url = "http://www.douxuedu.com/#/main/course"

    # 页面元素
    loginBt = ('xpath', '//*[@id="frame_box"]/header/header/div/span/span[3]')
    username = ('xpath', '//*[@id="frame_box"]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/p[1]/div/input')
    passport_e = ('xpath', '//*[@id="frame_box"]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/p[2]/div/input')
    loginBt2 = ('xpath', '//*[@id="frame_box"]/div[1]/div[1]/div[2]/div[2]')
    # 管理后台
    assert_element = ('xpath', '//*[@id="frame_box"]/header/header/div/span/span[3]/span')

    def get_page(self):
        self.driver.get(url=self.url)

    def login(self, username: str, password: str):
        self.element(*self.loginBt).click()
        self.element(*self.username).click()
        self.element(*self.username).send_keys(username)
        print(*self.passport_e)
        self.element(*self.passport_e).click()
        self.element(*self.passport_e).send_keys(password)
        self.element(*self.loginBt2).click()

