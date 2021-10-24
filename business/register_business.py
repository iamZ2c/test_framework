from handle.register_handle import RegisterHandle
import base.creat_phonenum
from base.redis_servers import Redis_server


class RegisterBusiness:
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver=driver)

    def normal_register(self):
        # 点击注册界面
        self.register_h.click_home_page_button()
        # 生成随机电话号码
        phone_num = base.creat_phonenum.get_random_phone_num()
        # 输入随机号码
        self.register_h.send_phone_num(phone=phone_num)
        # 点击发送验证码
        self.register_h.click_get_v_code()
        rs = Redis_server()
        # 在redis服务器里面获取输入电话号码的验证码
        v_code = rs.get_verification_code(phone_number=phone_num)
        # 输入验证码
        self.register_h.send_v_code(v_code=v_code)
        # 业务执行到这里就返回True，我们的case层只需要调用方法，知道true or false即可
        return True

    def assert_tip_text(self, key, text):
        self.register_h.click_home_page_button()
        self.register_h.click_next_step_button()
        if self.register_h.get_element_text(key=key) == text:
            return True
