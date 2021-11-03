# coding=utf-8

import time
import os
import sys
sys.path.append('G:/Git/pytest_testApi')
from data.data_opera import data_Op
from common.base import Page
from testCase.page_obj.element_opera import element_Op
sheet_name = 'addMerchant'

class res_Assert(Page):

    # 联系邮箱
    emailAs_loc = ("css selector", "#time01 > div:nth-child(4) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required.ivu-form-item-error > div > div.ivu-form-item-error-tip")
    def emailAs(self, except_result, i):
        opd = data_Op()
        try:
            text = self.get_text(self.emailAs_loc)
            if text == except_result:
                test_result1 = "通过"
                print(test_result1)
                opd.write_value(i, sheet_name, test_result1)
            else:
                test_result2 = "不通过"
                print(test_result2)
                opd.write_value(i, sheet_name, test_result2)

        # 后续需要继续优化，输入正确数据的情况下不应该放入except中
        except:
            test_result3 = "不通过"
            print(test_result3)
            opd.write_value(i, sheet_name, test_result3)

        # 获取输入框输入的文本
        """
          platcustomer_text = self.get_attribute(self.platcustomercode_loc1, 'value')
          print(platcustomer_text)
          plcustomer_code = data1[0]['platcustomercode']
          if plcustomer_code in platcustomer_text:
              print("平台商户输入成功")
          else:
              print("平台商户输入失败")
          """

    # 手机号
    # 联系邮箱
    mobileAs_loc = ("css selector",
                   "#time01 > div:nth-child(3) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required.ivu-form-item-error > div > div.ivu-form-item-error-tip")
    def mobileAs(self, except_result, i):
        opd = data_Op()
        try:
            text = self.get_text(self.mobileAs_loc)
            if text == except_result:
                test_result1 = "通过"
                print(test_result1)
                opd.write_value(i, sheet_name, test_result1)
            else:
                test_result2 = "不通过"
                print(test_result2)
                opd.write_value(i, sheet_name, test_result2)

        # 后续需要继续优化，输入正确数据的情况下不应该放入except中
        except:
            test_result3 = "通过"
            print(test_result3)
            opd.write_value(i, sheet_name, test_result3)