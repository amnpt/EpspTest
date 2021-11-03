import xlrd
from xlutils.copy import copy
from config import globalparam

class ExcelUtil():
    def __init__(self, execlPath, sheetName):
        self.data = xlrd.open_workbook(execlPath)
        self.table = self.data.sheet_by_name(sheetName)
        # Get the first row as the key value
        self.keys = self.table.row_values(0)
        # Get the total number of rows
        self.rowNum = self.table.nrows
        # Get the total number of columns
        self.colNum = self.table.ncols

    # 获取execl用例数据
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r



