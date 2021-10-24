import ddt
from business import register_business
from test_case.ydy_base_test_case import YdyBaseTestCase
from util.execel_util import ExcelUtil
from config import settings

eu = ExcelUtil()
execle_data = eu.get_data()


@ddt.ddt
class DataDrivenTestCase(YdyBaseTestCase):
    """
    数据驱动类，由于ddt，数据驱动的时候会改写方法名称，所以单独起子类一类，专门做数据驱动
    @ddt.data()
    @ddt.unpack()解压参数
    """

    def setUp(self):
        super().setUp()
        self.rb = register_business.RegisterBusiness(driver=self.driver)
        self.driver.get(settings.PROJECT_URL)

    def tearDown(self):
        super().tearDown()

    @ddt.data(*execle_data)
    def test_tip_text(self, data):
        key = data[0]
        assert_text = data[1]
        self.assertTrue(expr=self.rb.assert_tip_text(key=key, text=assert_text),
                        msg="用例'{}'检验失败".format("test_tip_text"))
