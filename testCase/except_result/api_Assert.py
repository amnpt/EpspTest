# coding=utf-8

import time
import json
import requests
from data.data_opera import data_Op
from common.base import Page
from testCase.page_obj.element_opera import element_Op
from common import Encrypt
from common.order import db_connect
from common.order import order_opera
from common import get_Config
from common import Log

logobj = Log.loggerClass('debug')

class api_Request():

    def request_interface(self, i, sheet_name, api_host, request_url, method, request_data, check_point):
        opd = data_Op()

        # 构造请求headers
        headers = {  'Content-Type': 'application/json; charset=UTF-8',
                        'x-efps-sign' : Encrypt.req_encrypt(request_data),
                       # 'x-efps-sign-no' : get_Config.get_signno_Conf()  # ApiPay
                        'x-efps-app-id': get_Config.get_signno_Conf1()  # CardPay
                        }
        # 判断请求方式，如果是GET，则调用get请求，POST调post请求，都不是，则抛出异常
        if method == "GET":
            r = requests.get(url=api_host+request_url, params=json.loads(request_data), headers=headers)
            resp = r.text
            result_json = r.json()  #引入json模板，将响应结果转变为字典格式
            return_Code = result_json['returnCode']  #获取响应返回的returnCode值
            return_Msg = result_json['returnMsg']
            if check_point == return_Code:  # 断言，判断预期值是否与响应参数returnCode一致
                test_result1 = "通过"
                print("get接口请求成功，结果返回值为\n{}. ". format(r.text))
                logobj.info("get接口请求成功，结果返回值为\n{}. ". format(r.text))
               # opd.api_write_value(i, sheet_name, actual_result = test_result1, returnCode = return_Code, returnMsg = return_Msg)  # 返回响应码
                opd.api_write_result(i, sheet_name, actual_result = test_result1, returnMsg = resp)  # 返回所有响应信息

                return resp
            else:
                test_result2 = "不通过"
                opd.api_write_value(i, sheet_name, actual_result = test_result2, returnCode = return_Code, returnMsg = return_Msg)
                print("get接口请求失败！！！结果返回值为\n{}.".format(r.text))
                logobj.info("get接口请求失败！！！结果返回值为\n{}.".format(r.text))

                return resp

        elif method == "POST":
            payload1 = json.dumps(request_data)         # 接受python的基本数据类型，然后将其序列化为string
            payload2 = json.loads(payload1)             # 接受一个合法字符串，然后将其反序列化为python的基本数据类型
            r = requests.post(url=api_host+request_url, data=payload2, headers=headers)
            resp = r.text
            result_json = r.json()  # 引入json模板，将响应结果转变为字典格式
            return_Code = result_json['returnCode']  # 获取响应返回的returnCode值
            return_Msg = result_json['returnMsg']
            if check_point == return_Code:              # 断言，判断预期值是否与响应参数returnCode一致
                test_result1 = "通过"
                print("post接口请求成功，结果返回值为\n{}.".format(r.text))
                logobj.info("post接口请求成功，结果返回值为\n{}.".format(r.text))
                opd.api_write_value(i, sheet_name, actual_result = test_result1, returnCode = return_Code, returnMsg = return_Msg)
                #opd.api_write_result(i, sheet_name, actual_result = test_result1, returnMsg = resp)  # 返回所有响应信息

                return resp
            else:
                test_result2 = "不通过"
                opd.api_write_value(i, sheet_name, actual_result = test_result2, returnCode = return_Code, returnMsg = return_Msg)
                #opd.api_write_result(i, sheet_name, actual_result = test_result2, returnMsg = resp)  # 返回所有响应信息

                print("post接口请求失败！！！结果返回值为\n{}.".format(r.text))
                logobj.info("post接口请求失败！！！结果返回值为\n{}.".format(r.text))
                return resp
        else:
            print("接口请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。")
            logobj.info("接口请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。")
            logobj.info(400, "请求方式有误")
            return 400, "请求方式有误"


