from faker.factory import Factory

fake = Factory().create('zh_CN')


def random_py_data():
    return fake.pystr(), \
           fake.pyint(), \
           fake.pyfloat(), \
           fake.pytuple(nb_elements=2), \
           fake.pydict(nb_elements=2),


def random_uuid():
    return fake.uuid4()


def random_img():
    return fake.image_url()


def random_text():
    return fake.text()


def random_file_path():
    return fake.file_path()


def random_os_info(os_type: str):
    if os_type == 'win':
        return fake.windows_platform_token() + ' ' + fake.linux_processor()
    if os_type == 'linux':
        return fake.linux_processor()
    if os_type == 'mac':
        return fake.mac_platform_token()
    if os_type == 'ios':
        return fake.ios_platform_token()
    if os_type == 'android':
        return fake.android_platform_token()
    return


def random_hash(raw_output: bool = False):
    """

    :param raw_output: 16位
    :return:
    """
    return {'md5': fake.md5(raw_output),
            'sha1': fake.sha1(raw_output),
            'sha256': fake.sha256(raw_output)
            }


def random_password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True):
    return fake.password(
        length=length,
        special_chars=special_chars,
        digits=digits,
        upper_case=upper_case,
        lower_case=lower_case
    )


def random_name():
    return fake.name()


def random_address():
    return fake.address()


def random_phone_number():
    return fake.phone_number()


def random_job():
    return fake.job()


def random_ssn(*args):
    """
    生成身份证
    :param args:最大年龄和最小年龄
    :return:
    """
    fake.ssn(*args)


def credit_card_full():
    """
    银行卡信息
    :return:
    """
    return fake.credit_card_full(), fake.credit_card_number()


def random_company():
    return fake.company()


def random_email():
    return fake.email()


def random_birth(minimum=18, maximum=20):
    return fake.date_of_birth(minimum_age=minimum, maximum_age=maximum)


def random_profile():
    return fake.profile()


def random_ip4(private=False, public=False):
    if private:
        return fake.ipv4_private()
    if public:
        return fake.ipv4_public()
    return fake.ipv4()


def random_ip6():
    return fake.ipv6()


def random_mac_address():
    return fake.mac_address()


def random_user_agent():
    return fake.user_agent()


def random_mime_type(mime_type: str = "application"):
    return fake.mime_type(mime_type)
