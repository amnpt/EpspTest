# -*- coding: utf-8 -*-
import requests
from common import get_Config


# 签名验证及加密请求参数
def req_encrypt(request):

    headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
                }

    url = get_Config.get_req_encrypt_Url()
    data = {'content': request}
    respson = requests.post(url, data)
    result_json = respson.json()   # 引入json模板，将响应结果转变为字典格式
    sign = result_json['sign']   # 获取响应返回的sign值
    # print(sign)
    # print(request)
    return sign


def auth_encrypt(request):
    headers = {'Content-Type': 'application/json; charset=UTF-8'
               }
    url = get_Config.get_auth_encrypt_Url()
    respson = requests.post(url = url, data = request, headers = headers)

    result_json = respson.json()
    bankCardNo = result_json['bankCardNo']
    bankUserName = result_json['bankUserName']
    bankUserCert = result_json['bankUserCert']

    return bankCardNo, bankUserName, bankUserCert

