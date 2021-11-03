#!/usr/bin/env python
#-*- coding:utf-8 -*-

# ---*---注释---*---
# 定义接口请求header信息

from common import get_Config
from common import Encrypt
from data import request_data


# 1、主扫普通交易请求headers
nativePay_headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'x-efps-sign': Encrypt.req_encrypt(request_data.nativePay_payload),
                   'x-efps-sign-no': get_Config.get_signno_Conf()
                   }

# 2、主扫分账交易-实时分账请求headers
nativeRealTimeSplit_headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'x-efps-sign': Encrypt.req_encrypt(request_data.nativeRealTimeSplit_payload),
                   'x-efps-sign-no': get_Config.get_signno_Conf()
                   }

# 3、主扫分账交易-延时分账请求headers
nativeDelaySplit_headers = {'Content-Type': 'application/json; charset=UTF-8',
                   'x-efps-sign': Encrypt.req_encrypt(request_data.nativeDelaySplit_payload),
                   'x-efps-sign-no': get_Config.get_signno_Conf()
                   }

# 4、延时分账请求headers，需要传入收单请求的outTradeNo，进行分账
def splitDetail_headers(outTradeNo):
    splitDetail_headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'x-efps-sign': Encrypt.req_encrypt(request_data.splitDetail(outTradeNo)),
                       'x-efps-sign-no': get_Config.get_signno_Conf()
                       }
    return splitDetail_headers

# 5、普通交易退款请求headers，需要传入outTradeNo，refund_amount 进行退款
def refund_headers(outTradeNo, refund_amount):
    refund_headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'x-efps-sign': Encrypt.req_encrypt(request_data.refund(outTradeNo, refund_amount)),
                       'x-efps-sign-no': get_Config.get_signno_Conf()
                       }
    return refund_headers

# 6、分账交易退款请求headers，需要传入outTradeNo，refund_amount,原分账金额split_amount1, split_amount2 进行退款
def split_refund_headers(outTradeNo, refund_amount, split_amount1, split_amount2):
    split_refund_headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'x-efps-sign': Encrypt.req_encrypt(request_data.split_refund(outTradeNo, refund_amount, split_amount1, split_amount2)),
                       'x-efps-sign-no': get_Config.get_signno_Conf()
                       }
    return split_refund_headers


# 7、账户分账请求headers
account_split_headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'x-efps-sign': Encrypt.req_encrypt(request_data.accountSplit_payload),
                       'x-efps-sign-no': get_Config.get_signno_Conf()
                       }

# 8、单笔代付请求headers
withdrawalToCard_headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'x-efps-sign': Encrypt.req_encrypt(request_data.withdrawalToCard_payload),
                       'x-efps-sign-no': get_Config.get_signno_Conf()
                       }

# 9、子商户提现请求headers
withdraw_subMerchant_headers = {'Content-Type': 'application/json; charset=UTF-8',
                       'x-efps-sign': Encrypt.req_encrypt(request_data.withdraw_subMerchant_payload),
                       'x-efps-sign-no': get_Config.get_signno_Conf()
                       }
