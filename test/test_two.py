
import xlrd
from xlwt import *
from xlutils.copy import copy

class test_write():
    def test_write_value(self):
        old_file = 'G:/8.python/pytest_testApi/data/test.xls'
        data = xlrd.open_workbook(old_file)
        print(data)
        data_copy = copy(data)
        # print("打印2")
        sheet_copy = data_copy.get_sheet(0)
        # print("打印3")
        sheet_copy.write(4,3,"pass")
        # print("打印4")
        data_copy.save(old_file)