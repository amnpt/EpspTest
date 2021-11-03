#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 主扫分账交易-实时分账，用于冒烟或者回归测试

import requests
import json
import time

from common import get_Config
from common.order import db_connect
from common.order import order_opera
from data import request_data
from data import header

# 单个测试用例调试
def test_nativeRealTimeSplit():
    try:
        response = requests.post(url = get_Config.get_mainScaning_Url(),
                                 data = request_data.nativeRealTimeSplit_payload,
                                 headers = header.nativeRealTimeSplit_headers)
        # print(api_data.nativeRealTimeSplit_payload)
        # print(get_Config.get_mainScaning_Url())
        result_json = response.json()
        print(result_json)
        return_Code = result_json['returnCode']
        out_Trande_No = result_json['outTradeNo']
        if return_Code == '0000':
            order_inq = db_connect.order_query(out_Trande_No)   # 查询transaction_no
            # print(order_inq)
            if len(order_inq) != 0:   # 判断是否生成transaction_no
                state_mod = order_opera.state_modify(order_inq)   # 修改clr表订单状态
                if state_mod == 'success':
                    print('修改clr状态成功')
                    time.sleep(3)
                    result_que = order_opera.result_query(order_inq)    # 查询交易状态
                    paystate = result_que['payState']
                    if paystate == '00':
                        print("实时分账收单流程正常")
                        acc_flow, sett_flow = db_connect.acc_sett_query(order_inq)    # 查询记账及结算流水
                        # print(acc_flow, sett_flow)
                        if len(acc_flow) != 0 and len(sett_flow) != 0:     # 判断记账及结算记录非空，则返回记录正常
                            print("实时分账收单记账及结算记录正常")
                            time.sleep(3)
                            # start 检查分账交易流水记录
                            split_orderState, split_transactionNo = db_connect.split_order_query(out_Trande_No)    # 查询分账订单状态及分账订单号
                            # print(split_orderState, split_transactionNo)
                            split_recordState = db_connect.split_record_query(split_transactionNo)  # 1、查询分账明细分账状态，2、split_recordState返回值是一个元组，需要用索引调用，我也不知道为什么
                            # print(split_recordState)
                            if split_orderState == '00' and split_recordState[0] == '3':
                                print("实时分账交易成功")
                                # start 检查分账记账及结算记录
                                split_acc_flow, split_sett_flow = db_connect.acc_sett_query(split_transactionNo)    # 查询分账交易记账及结算流水
                                print(split_acc_flow, split_sett_flow)
                                if len(split_acc_flow) != 0 and len(split_sett_flow) != 0:     # 判断记账及结算记录非空，则返回记录正常
                                    print("实时分账记账及结算记录正常")
                                elif len(split_acc_flow) != 0 and len(split_sett_flow) == 0:
                                    print("实时分账记账记录正常，结算记录为空")
                                elif len(split_acc_flow) == 0 and len(split_sett_flow) != 0:
                                    print("实时分账记账记录为空，结算记录正常")
                                elif len(split_acc_flow) == 0 and len(split_sett_flow) == 0:
                                    print("实时分账记账及结算记录为空")
                                else:
                                    print("实时分账记账及结算数据异常，请人工检查数据")
                                # end
                            elif split_orderState == '01' and split_recordState[0] == '2':
                                print("实时分账交易失败")
                            elif split_orderState == '03' and split_recordState[0] == '1':
                                print("实时分账未执行分账")
                            else:
                                print("实时分账数据异常，请人工检查！")
                            # end
                        elif len(acc_flow) != 0 and len(sett_flow) == 0:
                            print("记账记录正常，结算记录为空")
                        elif len(acc_flow) == 0 and len(sett_flow) != 0:
                            print("记账记录为空，结算记录正常")
                        elif len(acc_flow) == 0 and len(sett_flow) == 0:
                            print("记账及结算记录为空")
                        else:
                            print("记账及结算记录数据异常，请人工检查数据")
                    elif paystate == '01':
                        print("实时分账收单失败，请检查失败原因！")
                    else:
                        print("实时分账收单未返回终态，请检查错误原因！")
                else:
                    print("修改clr状态失败！")
            else:
                print("交易请求未生成paytransaction_no，请检查错误原因！")
        else:
            print("接口请求失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)

