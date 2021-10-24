from page.register_page import RegisterPage


class RegisterHandle:
    def __init__(self, driver):
        self.register_p = RegisterPage(driver=driver)

    def click_home_page_button(self):
        self.register_p.get_homepage_register_button_element().click()

    def send_phone_num(self, phone):
        self.register_p.get_phone_num_element().click()
        self.register_p.get_phone_num_element().send_keys(phone)

    def click_get_v_code(self):
        self.register_p.get_get_v_code_button_element().click()

    def send_v_code(self, v_code):
        self.register_p.get_input_v_code_element().click()
        self.register_p.get_input_v_code_element().send_keys(v_code)

    def click_next_step_button(self):
        self.register_p.get_next_step_button_element().click()

    def get_element_text(self, key):
        return self.register_p.get_tip_element(key=key).text


