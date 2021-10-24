from time import sleep
from selenium.webdriver import ActionChains
from browser.browser import CHROME
from page.base_page import Page
from icecream.icecream import ic


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
    hover_e = ('xpath', '/html/body/div[1]/div/header/header/div/span/span[2]/div/span')
    logoutBt = ('xpath', '//*[@id="frame_box"]/header/header/div/span/span[2]/ul/li[3]')
    sureBt = ('xpath', '//*[@id="my_modal_box"]/div/div[2]/div[2]')

    def get_page(self):
        self.driver.get(url=self.url)
        self.driver.maximize_window()

    def login(self, username: str, password: str):
        ic(username + "开始登录")
        self.element(*self.loginBt).click()
        self.element(*self.username).click()
        self.element(*self.username).send_keys(username)
        self.element(*self.passport_e).click()
        self.element(*self.passport_e).send_keys(password)
        self.element(*self.loginBt2).click()

    def log_out(self):
        ac = ActionChains(driver=self.driver)
        he = self.element(*self.hover_e)

        ac.move_to_element(he).perform()
        sleep(2)
        self.element(*self.logoutBt).click()
        sleep(2)
        self.element(*self.sureBt).click()
        sleep(3)
        ic("logout")
