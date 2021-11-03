# coding=utf-8
import sys
sys.path.append('G:/Git/pytest_testApi')
import unittest
import time
from selenium import webdriver
from common.myunit import MyTest
from common.base import Page
from common import get_Config
from common.login.verifyCode import verify_Code
from testCase.page_obj import loginPage

# 参数中加 MyTest，用作登录测试类
# class loginTest( MyTest, Page):

# 参数中不加MyTest，用到调用登录类
class loginTest(Page):

    # 自动识别并输入验证码
    @unittest.skip("跳过此用例")
    def test_login1(self):
        po = loginPage.login(self.driver)
        po.open_login()
        code = verify_Code(self.driver).get_code()
        print(code)
        po.user_login(get_Config.get_admin_Username(), get_Config.get_admin_Password(), code)


    # 手动输入验证码
    def test_login2(self):
        po = loginPage.login(self.driver)
        po.open_login()
        po.user_loginnoCode(get_Config.get_admin_Username(), get_Config.get_admin_Password())
