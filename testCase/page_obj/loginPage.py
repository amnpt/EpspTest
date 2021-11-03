# coding=utf-8
# 通过selenium获取验证码图片

import time
from common.base import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
from common import get_Config
import selenium.webdriver.support.ui as ui
import unittest, time, re
import pytesseract


# 继承unittest.TestCase类，从TestCase类继承是告诉unittest模式的方式，这是一个测试案例
class login(Page):
    """
    User login page
    """
    url = get_Config.get_admin_Url()

    login_username_loc = ("css selector", "body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(1) > div > div > input")
    login_password_loc = ("css selector", "body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(2) > div > div > input")
    login_vercode_loc = ("css selector", "body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(3) > div > div > div.ivu-col.ivu-col-span-17 > div > input")
    login_button_loc1 = ("css selector", "body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > button > span")
    login_button_loc2 = ("xpath", "/html/body/div[2]/div[2]/div/div/div[2]/div/button")
    login_success_loc = ("css selector", "#app > div > div.main-header > div.logo-box > span")

    # 定义登录函数，将登录作为公共调用的模块，进行数据传递，因此不需要导入webdriver模块
    def login_userName(self, username):
        self.clear_type(self.login_username_loc, username)
    def login_passWord(self, password):
        self.clear_type(self.login_password_loc, password)
    def login_verCode(self, vercode):
        self.clear_type(self.login_vercode_loc, vercode)
    def login_button1(self):
        # self.wait.until(lambda driver:login_button_loc2)
        self.click(self.login_button_loc1)
    def login_button2(self):
        # self.wait.until(lambda driver:login_button_loc2)
        self.click(self.login_button_loc2)

    def open_login(self):
        self.open()
        try:
            self.title = '易票联支付'   # 测试网站的Title
            assert self.title in self.get_title()
            print("登录页面打开成功")
        except:
            print("登录页面打开失败")

    # 自动输入验证码
    def user_login(self, username, password, vercode):
        """
        User name password login
        """
        self.login_userName(username)
        self.login_passWord(password)
        self.login_verCode(vercode)
        time.sleep(2)
        self.login_button2()

        # 判断是否登录成功
        try:
            # self.driver.find_element_by_css_selector('#app > div > div.main-header > div.logo-box > span')
            self.get_element(self.login_success_loc)
            print("登录成功")
        except:
            print("登录失败")

    # 用户输入验证码
    def user_loginnoCode(self, username, password):
        self.login_userName(username)
        self.login_passWord(password)
        time.sleep(8)
        # 判断是否登录成功
        try:
            self.get_element(self.login_success_loc)
            print("登录成功")
        except:
            print("登录失败")


