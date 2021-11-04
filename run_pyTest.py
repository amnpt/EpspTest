#!/usr/bin/python
# coding=utf-8

# pytest 框架执行测试用例
# 执行交易回归测试用例

import pytest
import unittest
import time
from common.Email import send_email
import cx_Oracle
from common import get_Config

username = get_Config.get_database_Username()
password = get_Config.get_database_Password()
database = get_Config.get_database_Url()



if __name__ == "__main__":
    report = 'G:/AutoTest/EpspAutoTest/report/report_' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + '.html'
    #pytest.main(["-s", "G:/Git/pytest_testApi/testCase/apiTest", "--pytest_report", report])
    pytest.main(["-s", "G:/AutoTest/EpspAutoTest/testCase/apiTest/test_refundApply.py", "--pytest_report", 'G:/AutoTest/EpspAutoTest/report/report_' + time.strftime("%Y-%m-%d",time.localtime(time.time())) + '.html'])
    #send_email(report)   #163邮箱，需要开启 IMAP/SMTP服务
