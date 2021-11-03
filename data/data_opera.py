# coding=utf-8
import xlrd
from xlwt import *
import xlwt
from xlutils.copy import copy
import os
from common.datainfo import ExcelUtil
from config import globalparam

class data_Op():

    filepath = globalparam.data_path + "/" + "addMerchant.xls"

    # 以列表形式获取execl测试用例数据（ui）
    def get_data(self, sheet):
        sheetName = sheet
        data = ExcelUtil(self.filepath, sheetName)
        data1 = data.dict_data()
        print(data1)
        return data1


    # 根据列名称获取列号
    def get_ColumnIndex(self, sheet_name, columnName):
        data = xlrd.open_workbook(self.filepath)
        table = data.sheet_by_name(sheet_name)
        columnIndex = None
        for i in range(table.ncols):
            if (table.cell_value(0, i) == columnName):
                columnIndex = i
                break
        # print(columnIndex)
        return columnIndex

    # 获取所有行数
    def get_rowNum(self, sheet_name):
        data = xlrd.open_workbook(self.filepath)
        table = data.sheet_by_name(sheet_name)
        rowNum = table.nrows
        return rowNum


    # 写入测试结果到execl用例中(ui)
    def write_value(self, i, sheet_name, actual_result):
        data = xlrd.open_workbook(self.filepath)
        data_copy = copy(data)
        sheet_copy = data_copy.get_sheet(0)   # 封装类应该不直接传入实参，待研究，优化为传入形参
        # sheet_copy.write(i+1, 28, actual_result)   # 直接输入行、列，写入成功
        # sheet_copy.write('AC'+str([i+1]) , actual_result)  # 使用A1表示法，无法写入
        col = self.get_ColumnIndex(sheet_name, 'actual_result')
        sheet_copy.write(i + 1, col, actual_result)
        data_copy.save(self.filepath)


    # 写入测试结果(响应码及响应信息)到execl用例中(api)
    def api_write_value(self, i, sheet_name, actual_result, returnCode, returnMsg):
        data = xlrd.open_workbook(self.filepath)
        data_copy = copy(data)
        sheet_copy = data_copy.get_sheet(2)
        col1 = self.get_ColumnIndex(sheet_name, 'actual_result')
        col2 = self.get_ColumnIndex(sheet_name, 'return_Code')
        col3 = self.get_ColumnIndex(sheet_name, 'return_Msg')

        sheet_copy.write(i + 1, col1, actual_result)
        sheet_copy.write(i + 1, col2, returnCode)
        sheet_copy.write(i + 1, col3, returnMsg)

        data_copy.save(self.filepath)

    # 写入测试结果(响应返回)到execl用例中(api)
    def api_write_result(self, i, sheet_name, actual_result, returnMsg):
        data = xlrd.open_workbook(self.filepath)
        data_copy = copy(data)
        sheet_copy = data_copy.get_sheet(1)
        col1 = self.get_ColumnIndex(sheet_name, 'actual_result')
        col2 = self.get_ColumnIndex(sheet_name, 'return_Msg')

        sheet_copy.write(i + 1, col1, actual_result)
        sheet_copy.write(i + 1, col2, returnMsg)

        data_copy.save(self.filepath)


    # 获取测试用例编号（暂时没用上）
    def get_testNo(self, i, j, sheet):
        testno_lis = []
        while i <= j:
            # testNo = data1[i]['test_no']
            testNo = self.addMerchant_data(sheet)
            testno_lis.append(testNo)
            i = i+1
            print(testno_lis)
        return testno_lis