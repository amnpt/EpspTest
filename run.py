#!/usr/bin/python
# coding=utf-8

# unittest 框架执行测试用例

import time
import unittest
from BeautifulReport import BeautifulReport
from config import globalparam
from common.Email import send_email

suite = unittest.defaultTestLoader.discover(start_dir=globalparam.test_case_path, pattern='test_*.py')

print(suite)

if __name__ == '__main__':

    result = BeautifulReport(suite)
    report = result.report(filename='EPSP自动化测试报告'+time.strftime('%Y%m%d%H%M%S', time.localtime()), description='EPSP自动化测试报告', report_dir=globalparam.report_path)
    # send_email(report)   由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败