#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 账户分账，用于冒烟或者回归测试

import requests
import json
import time

from common import get_Config
from common.order import db_connect
from common.order import order_opera
from data import request_data
from data import header

def test_accountSplit():
    try:
        response = requests.post(url = get_Config.get_accountSplit_Url(),
                                 data = request_data.accountSplit_payload,
                                 headers = header.account_split_headers)

        result_json = response.json()
        print(result_json)
        return_Code = result_json['returnCode']
        out_Trande_No = result_json['outTradeNo']
        if return_Code == '0000':
            order_inq = db_connect.order_query(out_Trande_No)   # 查询transaction_no
            # print(order_inq)
            if len(order_inq) != 0:   # 判断是否生成transaction_no
                split_orderState, split_transactionNo = db_connect.split_order_query(out_Trande_No)   # 查询分账订单
                split_recordState = db_connect.split_record_query(split_transactionNo)    # 查询分账明细记录
                if split_orderState == '00' and split_recordState[0] == '3':
                    print("账户分账流程正常")
                    split_acc_flow, split_sett_flow = db_connect.acc_sett_query(split_transactionNo)    # 查询账户分账记账及结算流水
                    print(split_acc_flow, split_sett_flow)
                    if len(split_acc_flow) != 0 and len(split_sett_flow) != 0:     # 判断记账及结算记录非空，则返回记录正常
                        print("账户分账记账及结算记录正常")
                    elif len(split_acc_flow) != 0 and len(split_sett_flow) == 0:
                        print("账户分账记账记录正常，结算记录为空")
                    elif len(split_acc_flow) == 0 and len(split_sett_flow) != 0:
                        print("账户分账记账记录为空，结算记录正常")
                    elif len(split_acc_flow) == 0 and len(split_sett_flow) == 0:
                        print("账户分账记账及结算记录为空")
                    else:
                        print("账户分账记账及结算数据异常，请人工检查数据")
                                # end
                elif split_orderState== '01' and split_recordState[0] == '2':
                    print("账户分账失败")
                elif split_orderState == '03' and split_recordState[0] == '1':
                    print("账户分账未执行分账")
                else:
                    print("账户分账数据异常，请人工检查！")
                            # end
            else:
                print("交易请求未生成paytransaction_no，请检查错误原因！")
        else:
            print("接口请求失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)

