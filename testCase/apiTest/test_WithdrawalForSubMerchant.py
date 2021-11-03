#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 子商户提现-网联提现成功，银联失败（回滚），用于冒烟或者回归测试

import requests
import json
import time

from common import get_Config
from common.order import db_connect
from common.order import order_opera
from data import request_data
from data import header

def test_withdrawalForSubMer():
    try:
        response = requests.post(url = get_Config.get_withdraw_subMerchant_Url(),
                                 data = request_data.withdraw_subMerchant_payload,
                                 headers = header.withdraw_subMerchant_headers)

        result_json = response.json()
        print(result_json)
        return_Code = result_json['returnCode']
        transaction_No = result_json['transactionNo']
        if return_Code == '0000':
            print("子商户提现请求成功")
            time.sleep(10)
            clr_state, channel_resp_code, channel_resp_msg = db_connect.clr_withdraw_query(transaction_No)      # 查询transaction_no
            print(clr_state, channel_resp_code, channel_resp_msg)
            #
            # start:检查上游返回情况
            if clr_state == '00' and channel_resp_code == '00000000':    # 测试数据设置了网联代付测试环境可以返回成功，正常情况下返回成功
                print("网联子商户提现上游返回成功！")

                # start：检查交易支付情况
                txs_state = db_connect.txs_withdraw_query(transaction_No)
                pay_state = db_connect.pay_withdraw_query(transaction_No)

                # print(txs_state, pay_state)
                if txs_state[0][0] == '00' and pay_state[0][0] == '00':
                    print("网联子商户提现交易成功！")

                    # start：检查记账及结算情况
                    acc_flow, sett_flow = db_connect.withdrawal_acc_sett_query(transaction_No)  # 查询记账及结算流水
                    print(acc_flow, sett_flow)

                    if len(acc_flow) != 0 and len(sett_flow) != 0:  # 判断记账及结算记录非空，则返回记录正常
                        print("子商户提现（成功）记账及结算记录正常")
                    elif len(acc_flow) != 0 and len(sett_flow) == 0:
                        print("子商户提现（成功）记账记录正常，结算记录为空")
                    elif len(acc_flow) == 0 and len(sett_flow) != 0:
                        print("子商户提现（成功）记账记录为空，结算记录正常")
                    elif len(acc_flow) == 0 and len(sett_flow) == 0:
                        print("子商户提现（成功）记账及结算记录为空")
                    else:
                        print("子商户提现（成功）记账及结算数据异常，请人工检查数据！")
                      # end： 检查记账及结算情况，完毕

                elif txs_state[0][0] == '01' and pay_state[0][0] == '01':
                    print("网联子商户提现交易失败！" + "错误信息：" + channel_resp_code, channel_resp_msg)
                elif txs_state[0][0] == '03' and pay_state[0][0] == '03':
                    print("网联子商户提现处理中，请稍后再查询！")
                else:
                    print("网联子商户提现交易系统内部交易异常，请检查原因！")
                # end：检查交易支付情况，完毕

            elif clr_state == '02' and channel_resp_code == '00000000':
                print("网联子商户提现上游未返回交易状态！")

            elif clr_state == '02' and channel_resp_code != '00000000':   # 此时走银联渠道，无法返回成功，修改clr状态，只做内部系统检验
                print("银联上游处理中,返回信息：" + channel_resp_code, channel_resp_msg)
                print("进行修改clr状态（失败），检查系统内部交易")

                state_mod = order_opera.withdrawaState_toFail_modify(transaction_No)    # 修改clr表订单状态
                if state_mod == 'success':
                    print('修改clr状态为失败')
                    time.sleep(3)

                    # start：检查交易支付情况
                    txs_state = db_connect.txs_withdraw_query(transaction_No)
                    pay_state = db_connect.pay_withdraw_query(transaction_No)
                    print(txs_state, pay_state)

                    if txs_state[0][0] == '00' and pay_state[0][0] == '00':
                        print("银联子商户提现系统内部交易成功！")

                    elif txs_state[0][0] == '01' and pay_state[0][0] == '01':
                        print("银联子商户提现交易失败（回滚）！")
                        # start：检查记账情况（提现失败不会生成结算记录）

                        customercode1 = get_Config.get_customercode_Conf()
                        customercode2 = get_Config.get_customercode_Conf2()
                        acc_type1 = db_connect.withdrawal_acc_toTail_query(customercode1, transaction_No)  # 查询扣费商户记账流水
                        acc_type2 = db_connect.withdrawal_acc_toTail_query(customercode2, transaction_No)  # 查询提现商户记账流水

                        # print(acc_type1, acc_type2)

                        if acc_type1 == 1 and acc_type2 ==1:  # 判断记账是否存在正常记账及回滚流水
                            print("子商户提现失败（回滚），提现金额及扣费金额记账流水正常")
                        elif acc_type1 == 1 and acc_type2 == 0:
                            print("子商户提现失败（回滚），扣费金额记账流水正常，提现金额记账异常，请检查原因")
                        elif acc_type1 == 0 and acc_type2 == 1:
                            print("子商户提现失败（回滚），提现金额记账流水正常，扣费金额记账异常，请检查原因")
                        elif acc_type1 == 0 and acc_type2 == 0:
                            print("子商户提现失败（回滚），提现金额及扣费金额记账异常，请检查原因")
                        else:
                            print("子商户提现失败（回滚）记账及结算数据异常，请人工检查数据")
                        # end： 检查记账情况，完毕

                    elif txs_state[0][0] == '03' and pay_state[0][0] == '03':
                        print("银联子商户提现处理中，请稍后再查询或检查异常！")
                    else:
                        print("银联子商户提现系统内部交易异常，请检查原因！")
                    # end：检查交易支付情况，完毕

                else:
                    print("修改clr状态失败！")
            elif clr_state == '03':
                print("排队中，未发到上游，请检查原因！")
            elif clr_state == '01':
                print("子商户提现失败，请检查原因！")
            else:
                print("交易异常，请检查异常原因！")
            # end:检查上游返回情况，完毕
        else:
            print("接口请求失败！！！结果返回值为\n{}.".format(response.text))

    except Exception as e:
        print(e)




