from selenium.webdriver.remote.webelement import WebElement


class Page:
    """
    页面基类
    """
    driver = None
    url = None

    def element(self, *lco: tuple) -> WebElement:
        """
        定位单个元素的方法
        :param lco: 传入tuple类型，定位方法和定位信息
        :return: 返回定位后的WebElement对象
        """
        return self.driver.find_element(*lco)

    def elements(self, *lco: tuple) -> list:
        """
            定位单个元素的方法
            :param lco: 传入tuple类型，定位方法和定位信息
            :return: 返回多个定位后的WebElement对象
        """
        return self.driver.find_elements(*lco)