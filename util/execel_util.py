import xlrd
import os
from xlutils.copy import copy


class ExcelUtil:
    """
    读取execle数据类型
    """

    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            excel_path = os.path.dirname(os.getcwd()) + "\\config\\tips_and_text.xls"
        if index is None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    def get_data(self):
        """
        :return:得到ddt可以使用的二维列表
        """
        value = []
        for i in range(0, self.get_lines()):
            col = self.table.row_values(i)
            value.append(col)
        return value

    def get_lines(self):
        # 获取所有行数
        rows = self.table.nrows
        return rows

    def get_value(self, row, col):
        value = self.table.cell(row, col).value
        return value

    def write_value(self, row, write_text):
        """
        :param row:写入的行数
        :return:None
        """
        read_value = self.data
        write_value = copy(read_value)
        write_value.get_sheet(0).write(row, 9, write_text)
        write_value.save(os.path.dirname(os.getcwd()) + '\\config\\test_case.xls')
