#!/usr/bin/env python
#-*- coding:utf-8 -*-
# 适用所有接口
import os
import requests
import json
import time
import sys
import unittest
from threading import Timer
from common import Log
from data.data_opera import data_Op
from testCase.except_result.api_Assert import api_Request

sheet_name = 'apiPay'
data1 = data_Op().get_data(sheet = sheet_name)

logobj = Log.loggerClass('debug')

class test_apiPay(unittest.TestCase):
    @classmethod
    def test_Pay(self):
        nrows = data_Op().get_rowNum(sheet_name)
        for i in range(0, nrows-1):
            # num = str(data1[i]['No']).replace("\n", "").replace("\r", "")
            # api_name = data1[i]['API Name'].replace("\n", "").replace("\r", "")
            api_host = data1[i]['Host'].replace("\n", "").replace("\r", "")
            request_url = data1[i]['Request Url'].replace("\n", "").replace("\r", "")
            method = data1[i]['Method'].replace("\n", "").replace("\r", "")
            # request_data_type = data1[i]['Request Data Type'].replace("\n", "").replace("\r", "")
            request_data = data1[i]['Request Data'].replace("\n", "").replace("\r", "")
            check_point = data1[i]['Check_Point'].replace("\n", "").replace("\r", "")
            # message = data1[i]['except_result'].replace("\n", "").replace("\r", "")
            logobj.info(api_host+request_url+method+request_data+check_point)
            try:
                    # 调用接口请求方法，后面会讲到
                resp = api_Request().request_interface(i, sheet_name, api_host, request_url, method, request_data, check_point)
                logobj.info(resp, 'info')
                if check_point not in resp:
                    print("接口请求失败")
                    logobj.info("接口请求失败")

            except Exception as e:
                print(e)
                logobj.debug(e)
                print("接口请求失败，请检查失败原因！")
                logobj.info("接口请求失败，请检查失败原因！")




