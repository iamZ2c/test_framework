import time
from base.redis_dao import POOL
import redis
import re


class Redis_server:

    def __init__(self):
        self.con = redis.Redis(connection_pool=POOL)

    def get_verification_code(self, phone_number):
        """

        :param phone_number:传入类型str,返回接收到的手机验证码
        :return:返回验证码(str),没拿到验证码会反复请求redis去获取验证码
        """

        try:
            value = "sms:{0}".format(phone_number)
            for times in range(0, 3):
                time.sleep(1)
                verification_code = self.con.get(value)
                vcode = re.compile(r"(\d+)").search(bytes.decode(verification_code)).group(1)
                if vcode is not None:
                    print("phone:{},code:{}".format(phone_number, verification_code))
                    return vcode
                break
        except TypeError:
            print("<未获取到验证码,请检查验证码是否已经发送>")
            raise TypeError



# 测试代码
# r = Redis_server()
# print(r.get_verification_code(17283120748))
