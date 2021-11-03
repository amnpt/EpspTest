#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 动态生成测试数据

import datetime

# 1、生成商户订单号
def get_outTradeNo():
    outTradeNo = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    # print(outTradeNo)
    return outTradeNo# 1、生成商户订单号

# 生成退款订单号
def get_outRefundNo():
    outRefundNo = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # print(outTradeNo)
    return outRefundNo

# 2、生成交易开始时间
def get_startTime():
    startTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # print(startTime)
    return startTime

# 3、生成支付方式 6：微信主扫支付  7：支付宝主扫支付 24：银联二维码主扫
method = [6, 7, 24]

# 微信支付
def get_payMethod6():
    payMethod6 = method[0]
    # print(payMethod)
    return payMethod6

# 支付宝
def get_payMethod7():
    payMethod7 = method[1]
    return payMethod7

# 银联二维码
def get_payMethod24():
    payMethod24 = method[2]
    return payMethod24

#get_outTradeNo()
#get_startTime()
get_payMethod6()
