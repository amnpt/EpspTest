#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 主扫分账交易退款，用于冒烟或者回归测试

import requests
import json
import time

from common import get_Config
from common.order import db_connect
from common.order import order_opera
from data import request_data
from data import header
from common import Log


logobj = Log.loggerClass('debug')

# 单个用例调试时使用
# def nativeSplit_Pay():
#     try:
#         response = requests.post(url = get_Config.get_mainScaning_Url(),
#                                  data = request_data.nativeRealTimeSplit_payload,
#                                  headers = header.nativeRealTimeSplit_headers)
#         print(request_data.nativeRealTimeSplit_payload)
#         logobj.debug(request_data.nativeRealTimeSplit_payload)
#         result_json = response.json()
#         print(result_json)
#         logobj.debug(result_json)
#         return_Code = result_json['returnCode']
#         out_Trande_No = result_json['outTradeNo']
#         amount = result_json['amount']
#         if return_Code == '0000':
#             order_inq = db_connect.order_query(out_Trande_No)   # 查询transaction_no
#             # print(order_inq)
#             if len(order_inq) != 0:   # 判断是否生成transaction_no
#                 state_mod = order_opera.state_modify(order_inq)   # 修改clr表订单状态
#                 if state_mod == 'success':
#                     print('修改clr状态成功')
#                     logobj.debug("修改clr状态成功")
#                     time.sleep(3)
#                     result_que = order_opera.result_query(order_inq)    # 查询交易状态
#                     paystate = result_que['payState']
#                     if paystate == '00':
#                         print("分账交易收单流程正常")
#                         # start 检查分账交易流水记录
#                         split_orderState, split_transactionNo = db_connect.split_order_query(out_Trande_No)  # 查询分账订单状态及分账订单号
#                         split_recordState = db_connect.split_record_query(split_transactionNo)  # 1、查询分账明细分账状态，2、split_recordState返回值是一个元组，需要用索引调用，我也不知道为什么
#                         # print(split_recordState)
#                         if split_orderState == '00' and split_recordState[0] == '3':
#                             print("分账交易成功")
#                             # print(out_Trande_No, amount)
#
#                             #获取原分账金额
#                             split_amount1, split_amount2 = db_connect.split_amnout_query(split_transactionNo)
#
#                             # 返回参数，给 test_splitRefund() 函数使用
#                             return out_Trande_No, amount, split_amount1, split_amount2
#
#                         elif split_orderState == "01" and split_recordState[0] == '2':
#                             print("分账交易失败")
#                         elif split_orderState == "03" and split_recordState[0] == '1':
#                             print("分账未执行分账")
#                         else:
#                             print("分账数据异常，请人工检查！")
#                     elif paystate == '01':
#                         print("收单交易失败，请检查失败原因！")
#                     else:
#                         print("收单交易未返回终态，请检查错误原因！")
#                 else:
#                     print("修改clr状态失败！")
#             else:
#                 print("交易请求未生成paytransaction_no，请检查错误原因！")
#         else:
#             print("接口请求失败！！！结果返回值为\n{}.".format(response.text))
#
#     except Exception as e:
#         print(e)
#         logobj.debug(e)

# 主扫分账
def nativeSplitPay():
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
        amount = result_json['amount']

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

                                    # 获取原分账金额
                                    split_amount1, split_amount2 = db_connect.split_amnout_query(split_transactionNo)

                                    # print(out_Trande_No, amount)
                                    # 返回商户订单号和交易金额，退款时调用
                                    return out_Trande_No, amount, split_amount1, split_amount2

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


def test_splitRefund():
    outTradeNo, refund_amount, split_amount1, split_amount2 = nativeSplitPay()
    # print(outTradeNo, refund_amount, split_amount1, split_amount2)
    req_url = get_Config.get_refund_apply_Url()
    req_data = request_data.split_refund(outTradeNo, refund_amount, split_amount1, split_amount2)
    req_headers = header.split_refund_headers(outTradeNo, refund_amount, split_amount1, split_amount2)

    try:
        response = requests.post(url = req_url, data = req_data, headers = req_headers)

        print(req_data)
        logobj.debug(req_data)
        result_json = response.json()
        print(result_json)
        logobj.debug(result_json)
        time.sleep(5)

        return_Code = result_json['returnCode']
        if return_Code == '0000':
            print("发起分账退款申请正常")
            transaction_No = result_json['transactionNo']
            print(transaction_No)
            # txs_state, pay_state, clr_state = db_connect.refund_order_query(transaction_No)  # 查询txs、pay、clr退款状态
            txs_split_state = db_connect.split_refund_query(transaction_No)  # 查询txs-split退款状态
            # print(txs_split_state)

            if txs_split_state[0][0] == '2' and txs_split_state[1][0] == '2':
                print("分账交易退款失败(回滚)")
                logobj.debug("分账交易退款失败(回滚)")

                # start 检查分账记账及结算记录
                customercode1 = get_Config.get_customercode_Conf()
                customercode2 = get_Config.get_customercode_Conf2()

                # START c查询退款记账及结算流水开始
                refund_acc_type1 = db_connect.split_refund_acc_query(customercode1, transaction_No)   # 查询分账商户1的退款失败记账流水
                # print(refund_acc_type1)
                refund_sett_type1 = db_connect.split_refund_sett_query(customercode1, transaction_No)   # 查询分账商户1的退款失败结算流水
                # print(refund_sett_type1)
                refund_acc_type2 = db_connect.split_refund_acc_query(customercode2, transaction_No)  # 查询分账商户2的退款失败记账流水
                # print(refund_acc_type2)
                refund_sett_type2 = db_connect.split_refund_sett_query(customercode2, transaction_No)  # 查询分账商户2的退款失败结算流水
                # print(refund_sett_type2)
                # end 查询退款记账及结算流程结束

                if refund_acc_type1 == 1 and refund_sett_type1 == 1 and refund_acc_type2 == 1 and refund_sett_type2 == 1:   # 判断记账及结算记录同时存在退款及回滚记录，则返回退款失败
                    print("分账交易退款失败(回滚)记账及结算流水正常")
                    logobj.debug("分账交易退款失败(回滚)记账及结算流水正常")
                else:
                    print("分账交易退款失败(回滚)记账及结算流水数据异常，请人工检查数据")

            elif txs_split_state[0][0] == '3' and txs_split_state[1][0] == '3':
                print("分账交易退款成功")
                # 检查acc sett流水：refund_acc_type1 == 1，refund_sett_type1=1

            elif txs_split_state[0][0] == '1' and txs_split_state[1][0] == '1':
                print("分账交易退款未执行")

            else:
                print("分账交易退款异常，请人工检查异常情况")
        else:
            print("分账交易退款申请失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)
        logobj.debug(e)







