from base.find_element import FindElement


class RegisterPage:
    def __init__(self, driver):
        self.fe = FindElement(driver=driver, node="RegisterElement")

    def get_homepage_register_button_element(self):
        element = self.fe.get_element(key="homepage_register_button")
        return element

    def get_phone_num_element(self):
        element = self.fe.get_element(key="input_phone_num")
        return element

    def get_get_v_code_button_element(self):
        element = self.fe.get_element(key="get_v_code_button")
        return element

    def get_input_v_code_element(self):
        element = self.fe.get_element(key="input_v_code")
        return element

    def get_next_step_button_element(self):
        element = self.fe.get_element(key="next_step_button")
        return element

    def get_tip_element(self, key, node="RegisterElement"):
        element = self.fe.get_element(key=key)
        return element

    # def get_phone_num_none_tip_element(self):
    #     element = self.fe.get_element(node="RegisterElement", key="phone_num_None_tip")
    #     return element
    #
    # def get_phone_num_error_tip_element(self):
    #     element = self.fe.get_element(node="RegisterElement", key="phone_num_error_tip")
    #     return element
