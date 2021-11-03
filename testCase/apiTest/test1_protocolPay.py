#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 主扫普通交易退款，用于冒烟或者回归测试

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

def protocolPayPre():
    try:
        response = requests.post(url = get_Config.get_mainScaning_Url(),
                                 data = request_data.nativePay_payload,
                                 headers = header.nativePay_headers)
        print(request_data.nativePay_payload)
        logobj.debug(request_data.nativePay_payload)
        result_json = response.json()
        print(result_json)
        logobj.debug(result_json)
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
                    logobj.debug("修改clr状态成功")
                    time.sleep(3)
                    result_que = order_opera.result_query(order_inq)    # 查询交易状态
                    paystate = result_que['payState']
                    if paystate == '00':
                        print("收单交易流程正常")
                        print(out_Trande_No,amount)
                        return out_Trande_No,amount

                    elif paystate == '01':
                        print("收单交易失败，请检查失败原因！")
                    else:
                        print("收单交易未返回终态，请检查错误原因！")
                else:
                    print("修改clr状态失败！")
            else:
                print("交易请求未生成paytransaction_no，请检查错误原因！")
        else:
            print("接口请求失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)
        logobj.debug(e)


def test1_protocolPayConfirm():
    outTradeNo, refund_amount = protocolPayPre()

    try:
        response = requests.post(url = get_Config.get_refund_apply_Url(),
                                 data = request_data.refund(outTradeNo, refund_amount),
                                 headers = header.refund_headers(outTradeNo, refund_amount))
        print(request_data.refund(outTradeNo, refund_amount))
        logobj.debug(request_data.refund(outTradeNo, refund_amount))
        result_json = response.json()
        print(result_json)
        logobj.debug(result_json)
        time.sleep(5)

        return_Code = result_json['returnCode']
        if return_Code == '0000':
            print("发起普通交易退款申请正常")
            transaction_No = result_json['transactionNo']
            print(transaction_No)
            txs_state, pay_state, clr_state = db_connect.refund_order_query(transaction_No)  # 查询txs、pay、clr退款状态

            print(txs_state, pay_state, clr_state)

            if txs_state[0][0] == '01' and pay_state[0][0] == '01' and clr_state[0][0] == '01':
                print("普通交易退款失败(回滚)")
                logobj.debug("普通交易退款失败(回滚)")

                # start 检查分账记账及结算记录
                refund_acc_type = db_connect.refund_acc_query(transaction_No)  # 查询退款失败记账流水
                refund_sett_type = db_connect.refund_sett_query(transaction_No)   # 查询退款失败结算流水

                if refund_acc_type == 1 and refund_sett_type == 1:  # 判断记账及结算记录同时存在退款及回滚记录，则返回退款失败
                    print("普通交易退款失败(回滚)记账及结算流水正常")
                    logobj.debug("普通交易退款失败(回滚)记账及结算流水正常")

                elif refund_acc_type == 0 and refund_sett_type == 1:
                    print("普通交易退款失败(回滚)记账流水数据异常，结算流水正常")

                elif refund_acc_type == 1 and refund_sett_type == 0:
                    print("普通交易退款失败(回滚)结算流水数据异常，记账流水正常")

                else:
                    print("普通交易退款失败(回滚)记账及结算流水数据异常，请人工检查数据")

            elif txs_state[0][0] == '00' or pay_state[0][0] == '00' and clr_state[0][0] == '00':
                print("普通交易退款成功")
                # 检查acc sett流水：refund_acc_type == 1，refund_sett_type=1

            elif txs_state[0][0] != '01' or pay_state[0][0] != '01' and clr_state[0][0] == '01':
                print("clr为失败，txs及pay非失败，请人工检查异常情况")

            elif txs_state[0][0] != '00' or pay_state[0][0] != '00' and clr_state[0][0] == '00':
                print("clr为成功，txs及pay非成功，请人工检查异常情况")

            elif clr_state[0][0] == '03':
                print("clr为处理中，请人工检查异常情况")

            elif clr_state[0][0] == '02':
                print("clr为未支付，请等待支付或人工检查异常情况")
            else:
                print("普通交易退款异常，请人工检查异常情况")
        else:
            print("普通交易退款申请失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)
        logobj.debug(e)







