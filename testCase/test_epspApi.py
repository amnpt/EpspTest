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
import pytest
import xlrd
import os
import requests
import json
import yaml
import smtplib
import time
import datetime
import sys
import cx_Oracle
import webbrowser
import pytestreport
import logging


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from threading import Timer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from common import Encrypt
from common import Email
from common import Log

def cases_in_excel(test_case_file):
    #workbook = xlrd.open_workbook(r'G:\8.python\ApiTest\data\test_data02.xlsx')   # 直接读取execl文件
    change_dir = os.chdir("G:/8.python/pytest_testApi/Params")  #切换工作目录
    test_case_file = os.path.join(os.getcwd(), test_case_file)   #获取修改后的工作目录
    print(test_case_file)
    if not os.path.exists(test_case_file):

        print("测试用例excel文件不存在或路径有误！")
        # 找不到指定测试文件，就退出程序 os.system("exit")是用来退出cmd的
        sys.exit()

    else:
        # 读取excel文件
        test_case = xlrd.open_workbook(test_case_file)
        # 获取第一个sheet，下标从0开始
        table = test_case.sheet_by_index(1)
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
                req_List = request_interface(num, api_name, api_host, request_url, method,
                                             request_data_type, request_data, check_point, message)
                #print(req_List)

                for req_msg in req_List:
                    transactionNno = req_msg[0]
                    businessCode = req_msg[1]
                    state = req_msg[2]

                if businessCode != 'AliNative':
                    # append只接收一个参数，所以要将四个参数括在一起，当一个参数来传递
                    # 请求失败，则向error_cases中增加一条记录
                    error_cases.append((transactionNno, businessCode, state, "发起交易异常"))
                    #print(error_cases)
            except Exception as e:
                print(e)
                print("订单{}交易失败，请检查失败原因！".format(transactionNno))
                    # 访问异常，也向error_cases中增加一条记录
                error_cases.append((transactionNno, businessCode, state, "发起交易异常"))
                #print(error_cases)
        return error_cases


def request_interface(num, api_name, api_host, request_url, method,
                    request_data_type, request_data, check_point, message):
    # 构造请求headers
    headers = {  'Content-Type': 'application/json; charset=UTF-8',
                     'x-efps-sign' : Encrypt.req_encrypt(request_data),
                     'x-efps-sign-no' : '20190906test10'
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
        try:
            payload1 = json.dumps(request_data)         # 接受python的基本数据类型，然后将其序列化为string
            payload2 = json.loads(payload1)             # 接受一个合法字符串，然后将其反序列化为python的基本数据类型
            r = requests.post(url=api_host+request_url, data=payload2, headers=headers)
            result_r_json = r.json()   # 引入json模板，将响应结果转变为字典格式
            print(result_r_json)
            outTradeNo = result_r_json['outTradeNo']
            return_Code = result_r_json['returnCode']
            casherUrl = result_r_json['casherUrl']
            print(casherUrl)
            if check_point == return_Code:              # 断言，判断预期值是否与响应参数returnCode一致
                # logger = Log.loggerClass('debug')
                # logger.debug("第{}条用例'{}'执行成功，结果返回值为\n{}.".format(num, api_name, r.text),'debug')
                print("第{}条用例'{}'执行成功，结果返回值为\n{}.".format(num, api_name, r.text))
                open_Website(casherUrl)       # 调用函数打开收银台并选择支付宝
                order_list = check_payMethod(outTradeNo)    # 调用函数检查是否选择正确的支付方式
                for order_msg in order_list:
                    #transaction_no = order_msg[0]
                    business_code =  order_msg[1]
                    #state = order_msg[2]
                    #print(business_code)
                    if business_code == 'AliNative':
                        print("支付方式选择正确！")
                    else:
                        print("支付方式选择错误！")
            else:
                print("第{}条用例'{}'执行失败！！！结果返回值为\n{}.".format(num, api_name, r.text))
            return order_list
            print(order_list)
        except Exception as e:
            print(e)
    else:
        print("第{}条用例'{}'请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。".format(num, api_name))
        return 400, "请求方式有误"


# 后台打开收银台并选择支付宝支付
def open_Website(url):
    # 创建chrome浏览器驱动,无头模式(后台打开收银台)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options = chrome_options)

    # 加载界面
    driver.get(url)
    time.sleep(2)

    #逐渐滚动浏览器窗口，令ajax逐渐加载
    # for i in range(0,10):
    #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    #     i += 1
    #     time.sleep(4)

    # 拿到页面源码
    html = driver.page_source
    #print(html)
    #driver.find_element_by_css_selector('body > div.main > div.main-body.j-main > div.main-content.j-platform-content > div > ul > li:nth-child(2) > img').click()  #支付宝
    driver.find_element_by_css_selector('body > div.main > div.main - body.j - main > div.main - content.j - platform - content > div > ul > li: nth - child(2) > img').click()  #支付宝
    # driver.find_element_by_css_selector('body > div.main > div.main-body.j-main > div.main-content.j-platform-content > div > ul > li:nth-child(1) > img').click()  #微信

    time.sleep(3)
    driver.quit()


# 连接数据库，查询支付方式是否选择成功
def check_payMethod(out_trade_no):
    #建立连接
    order_list = []
    conn = cx_Oracle.connect('efps01', 'efps01', '172.20.19.201:1521/testdb')
    cursor = conn.cursor()   #创建游标
    res = cursor.execute('select transaction_no,business_code,state from TXS_PAY_TRADE_ORDER where out_trade_no = \'{}\''.format(out_trade_no))  #此处也可以使用%r，因为%r会给字符串加了单引号，才能作为sql的查询条件
    data = res.fetchall()   #获取数据
    for transaction_no, business_code, state in data:
        if len(transaction_no) != 0:
            print("已选择支付方式")
        else:
            print("未选择支付方式")
        order_list.append((transaction_no, business_code, state))
        return order_list
    #print(order_list)
    cursor.close()   #关闭游标
    conn.close()   #关闭数据库连接


def test_getCase():
    # 执行所有测试用例，获取错误的用例
    error_cases = cases_in_excel("test_cashierPay_data.xlsx")
    #error_cases = get_error_cases()
    # 如果有错误接口，则开始构造html报告
    if len(error_cases) > 0:
        # html = '<html><body>接口自动化扫描，共有 ' + str(len(error_cases)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
        html = '<html><body>主扫交易自动化测试，共有 ' + str(len(error_cases)) + ' 个异常交易，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">易票联订单号</th><th style="width:200px;text-align:left">支付业务</th><th   style="text-align:left">交易状态</th><th   style="text-align:left">交易情况</th></tr>'
        for test in error_cases:
            # html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] + '</td></tr>'
            html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] + '</td></tr>'
        Email.send_email(html)
        print(html)
        with open ("G:/8.python/pytest_testApi/report/report.html", "w") as f:
            f.write(html)
    else:
        print("本次测试，所有用例全部通过")
        #send_email("本次测试，所有用例全部通过")

#
#
if __name__ == '__main__':
    #pytest.main(['--html=../report/report.html','test_cashierPay01.py'])
    # pytest.main(["-s", "test_epspApi.py", "--pytest_report", 'G:/8.python/pytest_testApi/report/report_' +datetime.datetime.today().strftime('%Y-%m-%d')+ '.html'])
    pytest.main(["-s", "test_epspApi.py", "--pytest_report", 'G:/8.python/pytest_testApi/report/report_' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + '.html'])

