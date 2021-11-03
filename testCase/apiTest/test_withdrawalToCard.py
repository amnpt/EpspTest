#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 单笔代付-交易成功，用于冒烟或者回归测试

import requests
import json
import time

from common import get_Config
from common.order import db_connect
from common.order import order_opera
from data import request_data
from data import header

def test_withdrawalForMer():
    try:
        response = requests.post(url = get_Config.get_withdrawalToCard_Url(),
                                 data = request_data.withdrawalToCard_payload,
                                 headers = header.withdrawalToCard_headers)
        print(request_data.withdrawalToCard_payload)
        result_json = response.json()
        print(result_json)
        return_Code = result_json['returnCode']
        transaction_No = result_json['transactionNo']
        if return_Code == '0000':
            print("单笔代付请求成功")
            time.sleep(10)
            clr_state, channel_resp_code, channel_resp_msg = db_connect.clr_withdraw_query(transaction_No)      # 查询transaction_no
            print(clr_state, channel_resp_code, channel_resp_msg)
            #
            # start:检查上游返回情况
            if clr_state == '00' and channel_resp_code == '00000000':    # 测试数据设置了网联代付测试环境可以返回成功，正常情况下返回成功
                print("网联单笔代付上游返回成功！")

                # start：检查交易支付情况
                txs_state = db_connect.txs_withdraw_query(transaction_No)
                pay_state = db_connect.pay_withdraw_query(transaction_No)

                # print(txs_state, pay_state)
                if txs_state[0][0] == '00' and pay_state[0][0] == '00':
                    print("网联单笔代付交易成功！")

                    # start：检查记账及结算情况
                    acc_flow, sett_flow = db_connect.withdrawal_acc_sett_query(transaction_No)  # 查询记账及结算流水
                    print(acc_flow, sett_flow)

                    if len(acc_flow) != 0 and len(sett_flow) != 0:  # 判断记账及结算记录非空，则返回记录正常
                        print("单笔代付记账及结算记录正常")
                    elif len(acc_flow) != 0 and len(sett_flow) == 0:
                        print("单笔代付记账记录正常，结算记录为空")
                    elif len(acc_flow) == 0 and len(sett_flow) != 0:
                        print("单笔代付记账记录为空，结算记录正常")
                    elif len(acc_flow) == 0 and len(sett_flow) == 0:
                        print("单笔代付记账及结算记录为空")
                    else:
                        print("单笔代付记账及结算数据异常，请人工检查数据！")
                      # end： 检查记账及结算情况，完毕

                elif txs_state[0][0] == '01' and pay_state[0][0] == '01':
                    print("网联单笔代付交易失败！" + "错误信息：" + channel_resp_code, channel_resp_msg)
                elif txs_state[0][0] == '03' and pay_state[0][0] == '03':
                    print("网联单笔代付处理中，请稍后再查询！")
                else:
                    print("网联单笔代付交易系统内部交易异常，请检查原因！")
                # end：检查交易支付情况，完毕

            elif clr_state == '02' and channel_resp_code == '00000000':
                print("网联单笔代付上游未返回交易状态！")

            elif clr_state == '02' and channel_resp_code != '00000000':   # 此时走银联渠道，无法返回成功，修改clr状态，只做内部系统检验
                print("银联上游处理中,返回信息：" + channel_resp_code, channel_resp_msg)
                print("进行修改clr状态（成功），检查系统内部交易")

                state_mod = order_opera.withdrawaState_modify(transaction_No)    # 修改clr表订单状态
                if state_mod == 'success':
                    print('修改clr状态为成功')
                    time.sleep(3)

                    # start：检查交易支付情况
                    txs_state = db_connect.txs_withdraw_query(transaction_No)
                    pay_state = db_connect.pay_withdraw_query(transaction_No)
                    if txs_state[0][0] == '00' and pay_state[0][0] == '00':
                        print("银联单笔代付系统内部交易成功！")

                        # start：检查记账及结算情况
                        acc_flow, sett_flow = db_connect.withdrawal_acc_sett_query(transaction_No)  # 查询记账及结算流水
                        print(acc_flow, sett_flow)
                        if len(acc_flow) != 0 and len(sett_flow) != 0:  # 判断记账及结算记录非空，则返回记录正常
                            print("单笔代付记账及结算记录正常")
                        elif len(acc_flow) != 0 and len(sett_flow) == 0:
                            print("单笔代付记账记录正常，结算记录为空")
                        elif len(acc_flow) == 0 and len(sett_flow) != 0:
                            print("单笔代付记账记录为空，结算记录正常")
                        elif len(acc_flow) == 0 and len(sett_flow) == 0:
                            print("单笔代付记账及结算记录为空")
                        else:
                            print("单笔代付记账及结算数据异常，请人工检查数据")
                        # end： 检查记账及结算情况，完毕

                    elif txs_state[0][0] == '01' and pay_state[0][0] == '01':
                        print("银联代付交易失败！")
                    elif txs_state[0][0] == '03' and pay_state[0][0] == '03':
                        print("银联代付处理中，请稍后再查询或检查异常！")
                    else:
                        print("银联代付系统内部交易异常，请检查原因！")
                    # end：检查交易支付情况，完毕

                else:
                    print("修改clr状态失败！")
            elif clr_state == '03':
                print("排队中，未发到上游，请检查原因！")
            elif clr_state == '01':
                print("单笔代付失败，请检查原因！")
            else:
                print("单笔代付交易异常，请检查异常原因！")
            # end:检查上游返回情况，完毕
        else:
            print("接口请求失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)




