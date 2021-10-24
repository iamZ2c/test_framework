import random


def get_random_phone_num():
    """

    :return:返回随机电话号码
    """
    phone_head_data = "135、136、137、138、139、147、148、150、151、152、157、158、159、165、172、178、182、183、184、187、188、198、197"
    phone_head_list = phone_head_data.split("、")
    # chioce函数，随机从列表拿一个出来
    phone_head = random.choice(phone_head_list)
    # sample函数使用1——9随机生成八位
    phone_body = "".join(random.sample('0123456789', 8))
    return "{0}{1}".format(phone_head, phone_body)


