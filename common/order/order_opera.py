# coding=utf-8

import requests
from common import get_Config

# 1、修改支付订单状态
def state_modify(transaction_no):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    url = get_Config.get_order_modify_Url()
    dayload = {
        #'transactionNo' : '%s' %(transaction_no),  #此处使用 %s，参数已有单引号，直接使用%s，不需加单引号
        'transactionNo': '{}'.format(transaction_no),   #使用format(a),最新规范
        'state' : '00'  # 使用单引号，只使用 00 的话，只上传数字0
    }
    respon = requests.post(url=url, params=dayload, headers=headers)
    result_json = respon.json()
    code = result_json['code']
    return  code


# 2、查询交易结果
def result_query(transaction_no):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    url = get_Config.get_order_result_Url()
    payload = {
        'transactionNo': '{}'.format(transaction_no),  # 此处也可使用 %s，加上单引号，
        'customerCode': get_Config.get_customercode_Conf()
    }
    respon = requests.get(url = url, params = payload, headers = headers)
    result_json = respon.json()
    #paystate = result_que['payState']        # 直接获取响应返回的paystate值
    #returnCode = result_que['returnCode']
    #returnMsg = result_que['returnMsg']
    return result_json   # 直接返回所有响应参数，调用函数后再根据需求获取某个响应参数


# 3、修改代付订单状态为成功
def withdrawaState_modify(transaction_no):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    url = get_Config.get_withdrawal_modify_Url()
    dayload = {
        #'transactionNo' : '%s' %(transaction_no),  #此处使用 %s，参数已有单引号，直接使用%s，不需加单引号
        'transactionNo': '{}'.format(transaction_no),   #使用format(a),最新规范
        'state' : '00'  # 使用单引号，只使用 00 的话，只上传数字0
    }
    respon = requests.post(url=url, params=dayload, headers=headers)
    result_json = respon.json()
    code = result_json['code']
    return  code

# 4、修改代付订单状态为成功
def withdrawaState_toFail_modify(transaction_no):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    url = get_Config.get_withdrawal_modify_Url()
    dayload = {
        #'transactionNo' : '%s' %(transaction_no),  #此处使用 %s，参数已有单引号，直接使用%s，不需加单引号
        'transactionNo': '{}'.format(transaction_no),   #使用format(a),最新规范
        'state' : '01'  # 使用单引号，只使用 00 的话，只上传数字0
    }
    respon = requests.post(url=url, params=dayload, headers=headers)
    result_json = respon.json()
    code = result_json['code']
    return  code
