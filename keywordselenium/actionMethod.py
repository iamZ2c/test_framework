import time
from selenium import webdriver
from base.find_element import FindElement


class ActionMethod:
    def __init__(self):
        self.driver = None

    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            print(111111111111)
            self.driver = webdriver.Edge()

    def get_url(self, url):
        self.driver.get(url=url)
        self.driver.maximize_window()

    def get_element(self, node, key):
        fe = FindElement(self.driver)
        element = fe.get_element(node=node, key=key)
        return element

    def send_value(self, node, key, value):
        element = self.get_element(key=key, node=node)
        element.click()
        element.send_keys(value)

    def click_element(self, node, key):
        element = self.get_element(key=key, node=node)
        element.click()

    def sleep_time(self, times):
        time.sleep(times)

    def close_browser(self):
        self.driver.close()

    def get_element_text(self, node, key):
        text = self.get_element(key=key, node=node).text
        return text

