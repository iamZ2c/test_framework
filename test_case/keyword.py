from util.execel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
import os


class KeywordCase:
    def __init__(self):
        self.am = ActionMethod()
        self.eu = ExcelUtil(os.path.dirname(os.getcwd()) + "\\config\\test_case.xls")

    def run_main(self):
        case_num = self.eu.get_lines()
        if case_num:
            # 解析execle数据
            for i in range(1, case_num):
                case_execute = self.eu.get_value(row=i, col=2)
                if case_execute in ('yes', 'y', "YES"):
                    method = self.eu.get_value(row=i, col=4)
                    element_node = self.eu.get_value(row=i, col=5)
                    element_key = self.eu.get_value(row=i, col=6)
                    value = self.eu.get_value(row=i, col=7)
                    self.run_method(method=method, node=element_node, key=element_key, send_value=value, rows=i)

    def run_method(self, method, send_value, node, key, rows):
        method_value = getattr(self.am, method)
        if send_value:
            if type(send_value) is float:
                method_value(node, key, str(int(send_value)))
            else:
                method_value(node, key, send_value)
        elif node and key:
            #
            result = method_value(node, key)
            if result:
                self.write_actual(text=result, rows=rows)
        else:
            # 兼容只有一个参数的方法
            method_value(key)

    def write_actual(self, text, rows):
        self.eu = ExcelUtil(os.path.dirname(os.getcwd()) + "\\config\\test_case.xls")
        self.eu.write_value(row=rows, write_text=text)


if __name__ == '__main__':
    # kw = KeywordCase()
    # kw.run_main()
    # kw.am.close_browser()