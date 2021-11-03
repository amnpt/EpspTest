#!/usr/bin/env python
#-*- coding:utf-8 -*-

#在test_case02基础上修改，修改返回错误信息

"""
需求：自动读取、执行excel里面的接口测试用例，测试完成后，返回错误结果并发送邮件通知。
一步一步捋清需求：
1、设计excel表格
2、读取excel表格
3、拼接url，发送请求
4、汇总错误结果、发送邮件
"""
import xlrd
import os
import requests
import json
import yaml
import smtplib
import time
import sys
import cx_Oracle
import pytest

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from threading import Timer
from common import Email
from common import Log
from common import Encrypt
from common import get_Config

logobj = Log.loggerClass('debug')

def cases_in_excel(test_case_file):

    change_dir = os.chdir("G:/8.python/pytest_testApi/Params")  #切换工作目录
    test_case_file = os.path.join(os.getcwd(), test_case_file)   #获取修改后的工作目录
    #print(test_case_file)
    if not os.path.exists(test_case_file):
        print("测试用例excel文件不存在或路径有误！")
        # 找不到指定测试文件，就退出程序 os.system("exit")是用来退出cmd的
        sys.exit()

    # 读取excel文件
    test_case = xlrd.open_workbook(test_case_file)
    # 获取第一个sheet，下标从0开始
    table = test_case.sheet_by_index(0)
    # 记录错误用例
    error_cases = []
    # 一张表格读取下来，其实就像个二维数组，无非是读取第一行的第几列的值，由于下标是从0开始，第一行是标题，所以从第二行开始读取数据
    for i in range(1, table.nrows):
        num = str(int(table.cell(i, 0).value)).replace("\n", "").replace("\r", "")  #获取第2行第1列的内容
        api_name = table.cell(i, 1).value.replace("\n", "").replace("\r", "")
        api_host = table.cell(i, 2).value.replace("\n", "").replace("\r", "")
        request_url = table.cell(i, 3).value.replace("\n", "").replace("\r", "")
        method = table.cell(i, 4).value.replace("\n", "").replace("\r", "")
        request_data_type = table.cell(i, 5).value.replace("\n", "").replace("\r", "")
        request_data = table.cell(i, 6).value.replace("\n", "").replace("\r", "")
        check_point = table.cell(i, 7).value.replace("\n", "").replace("\r", "")
        message = table.cell(i, 8).value.replace("\n", "").replace("\r", "")

        #list_data = [num, api_name, api_host, request_url, method, request_data_type, request_data, check_point, message]  # 将execl用例各字段转换为列表
        #print(list_data)
        #return list_data   # 返回列表，给其他函数调用
        try:
            # 调用接口请求方法，后面会讲到
            resp = request_interface(num, api_name, api_host, request_url, method, request_data_type, request_data, check_point, message)
            logobj.info(resp, 'info')
            print(resp)

            outTradeNo = resp['outTradeNo']
            transactionNo = resp['transactionNo']
            paystate = resp['payState']


            if paystate != '00':
                # append只接收一个参数，所以要将四个参数括在一起，当一个参数来传递
                # 请求失败，则向error_cases中增加一条记录
                if transactionNo == None:
                    transactionNo = '0'
                    error_cases.append((outTradeNo, transactionNo, paystate, "交易异常"))
                    logobj.info(error_cases,'info')
                else:
                    error_cases.append((outTradeNo, transactionNo, paystate, "交易异常"))
                    logobj.info(error_cases,'info')
        except Exception as e:
            print(e)
            #logobj.debug(e)
            print("订单{}交易失败，请检查失败原因！".format(outTradeNo))
            logobj.debug("订单{}交易失败，请检查失败原因！".format(outTradeNo))
                # 访问异常，也向error_cases中增加一条记录
            if transactionNo == None:
                transactionNo = '0'
                error_cases.append((outTradeNo ,  transactionNo , paystate  , "交易异常"))
                logobj.info(error_cases,'info')
            else:
                error_cases.append((outTradeNo ,  transactionNo , paystate  , "交易异常"))
                logobj.info(error_cases,'info')
            #print(error_cases)
    return error_cases



def request_interface(num, api_name, api_host, request_url, method,
                    request_data_type, request_data, check_point, message):
    # 构造请求headers
    headers = {  'Content-Type': 'application/json; charset=UTF-8',
                 'x-efps-sign' : Encrypt.req_encrypt(request_data),
                 # 'x-efps-sign-no': '20190906test10'
                 'x-efps-sign-no' : get_Config.get_signno_Conf()
                }
    # 判断请求方式，如果是GET，则调用get请求，POST调post请求，都不是，则抛出异常
    if method == "GET":
        r = requests.get(url=api_host+request_url, params=json.loads(request_data), headers=headers)
        result_json = r.json()  #引入json模板，将响应结果转变为字典格式
        return_Code = result_json['returnCode']  #获取响应返回的returnCode值
        if check_point == return_Code:  # 断言，判断预期值是否与响应参数returnCode一致
            print("第{}条用例'{}'执行成功，结果返回值为\n{}. ". format(num, api_name, r.text))
            return return_Code
        else:
            print("第{}条用例'{}'执行失败！！！结果返回值为\n{}.".format(num, api_name, r.text))
            return return_Code

    elif method == "POST":
        payload1 = json.dumps(request_data)         # 接受python的基本数据类型，然后将其序列化为string
        payload2 = json.loads(payload1)             # 接受一个合法字符串，然后将其反序列化为python的基本数据类型
        r = requests.post(url=api_host+request_url, data=payload2, headers=headers)
        result_r_json = r.json()  # 引入json模板，将响应结果转变为字典格式
        out_Trade_No = result_r_json['outTradeNo']    # 获取响应返回的outTradeNo值
        return_Code = result_r_json['returnCode']     # 获取响应返回的returnCode值
        if check_point == return_Code:              # 断言，判断预期值是否与响应参数returnCode一致
            logobj.debug("第{}个接口'{}'请求成功，结果返回值为\n{}.".format(num, api_name, r.text),'debug')
            #print("第{}个接口'{}'请求成功，结果返回值为\n{}.".format(num, api_name, r.text))
            order_inq = order_query(out_Trade_No)   # 调用函数连接数据库，查询transaction_no
            if len(order_inq) != 0:                 # 判断transaction_no是否为空
                state_mod = state_modify(order_inq) # 调用函数修改订单状态
                #print(state_mod)
                if state_mod == 'success':          # 判断code是否为success
                    logobj.debug('修改clr状态成功！','debug')
                    # print('修改clr状态成功！')
                    #t = Timer(1.0, result_query)   # 指定1秒后执行result_query函数
                    #t.start()
                    result_que = result_query(order_inq)
                    paystate = result_que['payState']        # 直接获取响应返回的paystate值
                    #returnCode = result_que['returnCode']
                    #returnMsg = result_que['returnMsg']
                    if paystate == '00':
                        logobj.debug('交易成功','debug')
                        print("交易成功" )
                        return result_que
                    elif paystate == '01':
                        logobj.debug("交易失败，请检查失败原因！",'debug')
                        print("交易失败，请检查失败原因！")
                        return result_que
                    else:
                        logobj.debug("交易未返回终态，请检查错误原因！",'debug')
                        print("交易未返回终态，请检查错误原因！")
                        return result_que
                else:
                    print('修改clr状态失败！')
            else:
                print("交易请求未生成transaction_no，请检查错误原因！")
        else:
            print("第{}个接口'{}'请求失败！！！结果返回值为\n{}.".format(num, api_name, r.text))
    else:
        print("第{}个接口'{}'请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。".format(num, api_name))
        return 400, "请求方式有误"


# 连接数据库，查询交易订单号
def order_query(out_trade_no):
    #建立连接
    conn = cx_Oracle.connect('efps01', 'efps01', '172.20.19.201:1521/testdb')
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select transaction_no,state from TXS_PAY_TRADE_ORDER where out_trade_no = \'{}\''.format(out_trade_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    data = res.fetchall()   #获取数据
    for transaction_no, state in data:
        return transaction_no
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接


# 修改订单状态
def state_modify(transaction_no):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    url = 'http://172.20.4.90:8100/ArtificialModification'
    dayload = {
        #'transactionNo' : '%s' %(transaction_no),  #此处使用 %s，参数已有单引号，直接使用%s，不需加单引号
        'transactionNo': '{}'.format(transaction_no),   #使用format(a),最新规范
        'state' : '00'  # 使用单引号，只使用 00 的话，只上传数字0
    }
    respon = requests.post(url=url, params=dayload, headers=headers)
    result_json = respon.json()
    code = result_json['code']
    return  code

# 查询交易结果
def result_query(transaction_no):
    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    url = 'http://172.20.4.90:8110/pay/paymentQuery'
    payload = {
        'transactionNo': '{}'.format(transaction_no),  # 此处也可使用 %s，加上单引号，
        'customerCode': get_Config.get_customercode_Conf()
    }
    respon = requests.get(url = url, params = payload, headers = headers)
   # respon = requests.get(url, payload, headers)    # 传参只用payload请求不成功，换成params = payload才可以，暂时没有找到原因
    result_json = respon.json()
    #paystate = result_que['payState']        # 直接获取响应返回的paystate值
    #returnCode = result_que['returnCode']
    #returnMsg = result_que['returnMsg']
    return result_json   # 直接返回所有响应参数，调用函数后再根据需求获取某个响应参数



def test_getCase():
    # 执行所有测试用例，获取错误的用例
    error_cases = cases_in_excel("test_cashierPay_data.xlsx")
    #error_cases = get_error_cases()
    # 如果有错误接口，则开始构造html报告
    if len(error_cases) > 0:
        # html = '<html><body>接口自动化扫描，共有 ' + str(len(error_cases)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
        html = '<html><body>主扫交易自动化测试，共有 ' + str(len(error_cases)) + ' 个异常交易，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">外部订单号</th><th style="width:200px;text-align:left">易票联订单号</th><th   style="text-align:left">交易状态</th><th   style="text-align:left">交易情况</th></tr>'
        for test in error_cases:
            # html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] + '</td></tr>'
            html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] + '</td></tr>'
        #Email.send_email(html)
        print(html)
        logobj.debug(html)
        with open ("G:/8.python/pytest_testApi/report/report.html", "w") as f:
            f.write(html)
    else:
        logobj.debug("本次测试，所有用例全部通过",'debug')
        print("本次测试，所有用例全部通过")
        #send_email("本次测试，所有用例全部通过")



if __name__ == "__main__":
    # pytest.main(["-s", "test_epspNativePay.py", "--pytest_report", 'G:/8.python/pytest_testApi/report/report_' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + '.html'])
    pytest.main(["-s", "test_epspNativePay.py", "--pytest_report", 'G:/8.python/pytest_testApi/report/report_' + time.strftime("%Y-%m-%d",time.localtime(time.time())) + '.html'])


