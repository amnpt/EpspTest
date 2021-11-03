#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 主扫普通交易，用于冒烟或者回归测试

import unittest
import requests
import json
import time


from common import get_Config
from common.order import db_connect
from common.order import order_opera
from data import request_data
from data import header

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("unittest每个用例前置")

    def tearDown(self) -> None:
        print("unittest每个用例后置")

    @classmethod
    def setUpClass(cls) -> None:
        print("所有用例前置")
        # conn = cx_Oracle.connect(username, password, database)
        # cursor = conn.cursor()  # 创建游标

    @classmethod
    def tearDownClass(cls) -> None:
        print("所有用例后置")
        # cursor.close()  # 关闭游标
        # conn.close()  # 关闭数据库连接


    # 单个测试用例调试
    def test_nativePay(self):
        try:
            response = requests.post(url = get_Config.get_mainScaning_Url(),
                                     data = request_data.nativePay_payload,
                                     headers = header.nativePay_headers)
            print(request_data.nativePay_payload)
            # print(headers)
            result_json = response.json()
            print(result_json)
            return_Code = result_json['returnCode']
            out_Trande_No = result_json['outTradeNo']
            amount = result_json['amount']

            if return_Code == '0000':
                order_inq = db_connect.order_query(out_Trande_No)      # 查询transaction_no
                # print(order_inq)
                if len(order_inq) != 0:   # 判断是否生成transaction_no
                    state_mod = order_opera.state_modify(order_inq)    # 修改clr表订单状态
                    if state_mod == 'success':
                        print('修改clr状态成功')
                        time.sleep(3)
                        result_que = order_opera.result_query(order_inq)     # 查询交易状态
                        paystate = result_que['payState']
                        if paystate == '00':
                            print("普通交易流程正常")
                            acc_flow, sett_flow = db_connect.acc_sett_query(order_inq)     # 查询记账及结算流水
                            print(acc_flow, sett_flow)
                            if len(acc_flow) != 0 and len(sett_flow) != 0:     # 判断记账及结算记录非空，则返回记录正常

                                self.assertNotEqual(len(acc_flow), 0, msg="测试不通过") \
                                and self.assertNotEqual(len(sett_flow), 0, msg="测试不通过")    #unnittest断言
                                print("普通交易记账及结算记录正常")
                                print("测试通过")

                            elif len(acc_flow) != 0 and len(sett_flow) == 0:
                                print("普通交易记账记录正常，结算记录为空")
                            elif len(acc_flow) == 0 and len(sett_flow) != 0:
                                print("普通交易记账记录为空，结算记录正常")
                            elif len(acc_flow) == 0 and len(sett_flow) == 0:
                                print("普通交易记账及结算记录为空")
                            else:
                                print("普通交易记账及结算数据异常，请人工检查数据")
                        elif paystate == '01':
                            print("普通交易失败，请检查失败原因！")
                        else:
                            print("交易未返回终态，请检查错误原因！")
                    else:
                        print("修改clr状态失败！")
                else:
                    print("交易请求未生成paytransaction_no，请检查错误原因！")
            else:
                print("接口请求失败！！！结果返回值为\n{}.".format(response.text))

        except Exception as e:
            print(e)




