#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 定义接口请求参数

from common import get_Config
from common import Encrypt
from data import get_date
import json

# 1、主扫-普通交易 请求参数
nativePay_params = {
        "attachData" : "普通交易回归测试",
        "channelType" : "01",
        "clientIp" : "127.0.0.1",
        "customerCode" : get_Config.get_customercode_Conf(),
        "noCreditCards" : "false",
        "nonceStr" : "48b099c9b1cc4f0b94d2a703da9251c8",
        "notifyUrl" : "http://www.baidu.com",
        "orderInfo" : {"businessType" : "test",
        "goodsList" : [{"amount":10,
        "category" : "test",
        "goodsId" : "6945726400021",
        "name" : "coffee",
        "number" : "1",
        "price" : 1,
        "remark" : "coffce"}],
        "id" : "test"},
        "outTradeNo" : get_date.get_outTradeNo(),
        "payAmount" : 10,
        "payCurrency" : "CNY",
        "payMethod" : get_date.get_payMethod7(),
        "redirectUrl" : "http://www.baidu.com",
        "subCustomerCode" : "",
        "terminalNo" : "10001",
        "transactionEndTime" : "",
        "transactionStartTime" : get_date.get_startTime()
        }

nativePay_payload= json.dumps(nativePay_params)  # 接受python的基本数据类型，然后将其序列化为string

# 2、主扫-实时分账 请求参数
nativeRealTimeSplit_params = {
        "attachData" : "实时分账回归测试",
        "channelType" : "01",
        "clientIp" : "127.0.0.1",
        "customerCode" : get_Config.get_customercode_Conf(),
        "needSplit" : "true",
        "noCreditCards" : "false",
        "nonceStr" : "7baca7f2c93847dd91ce9d6685a86685",
        "notifyUrl" : "http://www.baidu.com",
        "orderInfo" :
            {"businessType" : "test",
        "goodsList" : [{"amount" : 10,
             "category" : "类目1",
             "goodsId" : "6945726400021",
             "name" : "摩卡",
             "number" : "1",
             "price" : 1,
             "remark" : "优惠商品"}],
             "id" : "test"},
        "outTradeNo" : get_date.get_outTradeNo(),
        "payAmount" : 20,
        "payCurrency" : "CNY",
        "payMethod" : get_date.get_payMethod7(),
        "redirectUrl" : "http://www.baidu.com",
        "splitAttachData" : "0cf39844971449219c4a131e55464c36",
        "splitInfoList" : [{"amount":12,
             "customerCode" : get_Config.get_customercode_Conf(),
             "isProcedureCustomer" : 1},
            {"amount" : 8,
            "customerCode" : get_Config.get_customercode_Conf2(),
            "isProcedureCustomer" : 2}],
        "splitMain" : get_Config.get_customercode_Conf(),
        "splitModel" : "1",
        "splitNotifyUrl" : "http://www.baidu.com",
        "subCustomerCode" : "",
        "terminalNo" : "10001",
        "transactionEndTime" : "",
        "transactionStartTime" : get_date.get_startTime(),
        "version" : "3.0"
        }

nativeRealTimeSplit_payload = json.dumps(nativeRealTimeSplit_params)


# 3、主扫-延时分账 请求参数
nativeDelaySplit_params = {
        "attachData" : "延时分账（收单）回归测试",
        "channelType" : "01",
        "clientIp" : "127.0.0.1",
        "customerCode" : get_Config.get_customercode_Conf(),
        "needSplit" : "true",
        "noCreditCards" : "false",
        "nonceStr" : "f05071fe8d9f483c9551f8c714273ba9",
        "notifyUrl" : "http://www.baidu.com",
        "orderInfo" : {"businessType" : "test",
        "goodsList" : [{"amount":10,
        "category" : "类目1",
        "goodsId" : "6945726400021",
        "name" : "摩卡",
        "number" : "1",
        "price" : 1,
        "remark" : "优惠商品"}],
        "id" : "test"},
        "outTradeNo" : get_date.get_outTradeNo(),
        "payAmount" : 20,
        "payCurrency" : "CNY",
        "payMethod" : get_date.get_payMethod7(),
        "redirectUrl":"http://www.baidu.com",
        "splitMain" : get_Config.get_customercode_Conf(),
        "splitModel" : "1",
        "subCustomerCode" : "",
        "terminalNo" : "10001",
        "transactionEndTime" : "",
        "transactionStartTime" : get_date.get_startTime(),
        "version" : "3.0"
        }
nativeDelaySplit_payload = json.dumps(nativeDelaySplit_params)

# 4、延时分账 请求参数，需要传入收单请求的outTradeNo，进行分账
def splitDetail(outTradeNo):
    splitDetail_params = {
        "attachData" : "延时分账回归测试",
        "customerCode" : get_Config.get_customercode_Conf(),
        "nonceStr" : "fad3da9a054948c1ba7cc486c3aa266d",
        "notifyUrl" : "http://www.baidu.com",
        "outTradeNo" : outTradeNo,
        "splitInfoList" : [{"amount":12,
        "customerCode" : get_Config.get_customercode_Conf(),
        "isProcedureCustomer" : 1},
        {"amount": 8,
        "customerCode" : get_Config.get_customercode_Conf2(),
        "isProcedureCustomer" : 2}],
        "version" : "2.0"
        }
    splitDetail_payload = json.dumps(splitDetail_params)
    return  splitDetail_payload

# 5、普通交易退款 请求参数，需要传入outTradeNo，refund_amount 进行退款
def refund(outTradeNo, refund_amount):
    refund_params = {
        "amount" : refund_amount,
        "customerCode" : get_Config.get_customercode_Conf(),
        "nonceStr" : "15696cec8b2044729f17e9df12736cc1",
        "notifyUrl" : "http://www.baidu.com",
        "orderInfo" : {"businessType":"test",
        "goodsList" : [{"amount":10,
        "category" : "类目1",
        "goodsId" : "6945726400021",
        "name" : "摩卡",
        "number" : "1",
        "price" : 1,
        "remark" : "优惠商品"}],
        "id":"test"},
        "outRefundNo" : get_date.get_outRefundNo(),
        "outTradeNo" : outTradeNo,
        "refundAmount" : refund_amount,
        "remark" : "普通交易退款回归测试",
        "sourceChannel" : "API",
        # "transactionNo" : "",
        }
    refund_payload = json.dumps(refund_params)
    return  refund_payload

# 6、分账交易退款 请求参数，需要传入outTradeNo，refund_amount，原分账金额split_amount1, split_amount2 进行退款
def split_refund(outTradeNo, refund_amount, split_amount1, split_amount2):
    split_refund_params = {
        "amount" : refund_amount,
        "customerCode" : get_Config.get_customercode_Conf(),
        "nonceStr" : "e07b576c031f40539faf46164ffa09d0",
        "notifyUrl" : "http://www.baidu.com",
        "outRefundNo" : get_date.get_outRefundNo(),
        "outTradeNo" : outTradeNo,
        "refundAmount" : refund_amount,
        "remark" : "分账交易退款回归测试",
        "splitInfoList" : [
        {"amount": split_amount1,
        "customerCode" : get_Config.get_customercode_Conf(),
        "isProcedureCustomer" : 1},
        {"amount" : split_amount2,
        "customerCode" : get_Config.get_customercode_Conf2(),
        "isProcedureCustomer" : 0}],
        "transactionNo" : ""
                }
    split_refund_payload = json.dumps(split_refund_params)
    return  split_refund_payload

# 7、账户分账请求参数
accountSplit_params = {
        "attachData" : "账户分账回归测试",
        "commodityAmount" : 12,
        "commodityInfoList" : [{"commodityDescription":"红茶拿铁",
        "commodityOrderAmount" : 12,
        "commodityOrderNo" : "accS" + get_date.get_outTradeNo(),
        "commodityOrderTime" : get_date.get_startTime()}],
        "customerCode" : get_Config.get_customercode_Conf(),
        "nonceStr" : "9e95cb6d68384d9fb92cbeee27f64dc5",
        "notifyUrl" : "http://www.epaytest.cn/www/index.jsp",
        "outTradeNo" : "accsplit" + get_date.get_outTradeNo(),
        "splitInfoList" : [{"amount":9,
        "customerCode" : get_Config.get_customercode_Conf(),
        "isProcedureCustomer" : 0},
        {"amount" : 3,
        "customerCode" : get_Config.get_customercode_Conf2(),
        "isProcedureCustomer" : 0}],
        "version" : "1.0"
        }
accountSplit_payload = json.dumps(accountSplit_params)


# 8、持卡人信息
bankCardInfo_params = {
        "bankCardNo":"6214851111111111",
        "bankUserName":"郑小简",
        "bankUserCert":"44120019990917012x"
        }
bankCardInfo_payload = json.dumps(bankCardInfo_params)


bankCardInfo_params1={
        "bankCardNo":"6212142000000000012",
        "bankUserName":"中银联",
        "bankUserCert":"44120019990917012x"}
bankCardInfo_payload1 = json.dumps(bankCardInfo_params1)


bankCardInfo_params2={
        "bankCardNo":"2402008809200147996",
        "bankUserName":"贵州企多多科技有限公司",
        "bankUserCert":"44120019990917012x"}
bankCardInfo_payload2 = json.dumps(bankCardInfo_params2)


# 9、单笔代付请求参数
bankCardNo, bankUserName, bankUserCert = Encrypt.auth_encrypt(bankCardInfo_payload)
print(bankCardNo)
print(bankUserName)
withdrawalToCard_params = {
        "amount" : 10,
        "bankAccountType" : "2",
        "bankCardNo" : bankCardNo,
        "bankCity" : "广州市",
        "bankName" : "招商银行",
        "bankNo" : "303581038755",
        "bankProvince" : "广东省",
        "bankSub" : "招商银行广州分行体育东路支行",
        "bankUserCert" : bankUserCert,
        "bankUserName" : bankUserName,
        "customerCode" : get_Config.get_customercode_Conf(),
        "isAdvanceFund" : "0",
        "isFullAmount" : 0,
        "nonceStr" : "4103311220d04857bf6b70c40cba171e",
        "notifyUrl" : "http://172.20.18.116:8080/demo/notify/WithdrawalForSubMerchant",
        "outTradeNo" : get_date.get_outTradeNo(),
        "payCurrency" : "CNY",
        "remark" : "单笔代付回归测试"
        }
withdrawalToCard_payload = json.dumps(withdrawalToCard_params)


# 10、子商户提现请求参数
withdraw_subMerchant_params = {
        "bankCardId" : "1084619",
        "customerCode" : get_Config.get_customercode_Conf(),
        "isFullAmount" : 0,
        "memberId" : get_Config.get_customercode_Conf2(),
        "nonceStr" : "7f430eaa15794ff9a700c1c4e1d07c5a",
        "notifyUrl" : "www.baidu.com",
        "outTradeNo" : get_date.get_outTradeNo(),
        "payAmount" : 10,
        "payCurrency" : "CNY",
        "procedureCustomerCode" : get_Config.get_customercode_Conf(),
        "remark" : "子商户提现回归测试",
        "serviceFee" : 2,
        "subCustomerCode" : get_Config.get_customercode_Conf2(),
        "version" : "3.0"
        }
withdraw_subMerchant_payload= json.dumps(withdraw_subMerchant_params)

