# coding=utf-8

# 通过selenium获取验证码图片

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
from PIL import Image
import selenium.webdriver.support.ui as ui
import unittest, time, re
import pytesseract
from common.login import Tesseract
from config import globalparam


# 继承unittest.TestCase类，从TestCase类继承是告诉unittest模式的方式，这是一个测试案例
class Loginfor():
    # 封装
    def __init__(self, driver):
        self.driver = driver

    def get_code(self):
        driver = self.driver
        #driver.get(self.base_url)
        #driver.maximize_window()
        driver.save_screenshot(globalparam.auto_path+'/'+'All.png')  # 截取当前网页，该网页有我们需要的验证码
        imgelement = driver.find_element_by_class_name('code-img')

        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                    int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open(globalparam.auto_path+'/'+'All.png')  # 打开截图
        result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        result = result.convert('RGB')  # RGBA意思是红色，绿色，蓝色，Alpha的色彩空间，Alpha指透明度。而JPG不支持透明度，所以要么丢弃Alpha,要么保存为.png文件
        result_size = result.resize((140, 80))
        result_size.save(globalparam.auto_path+'/'+'result.jpg')  # 保存验证码图片
        time.sleep(5)
        image = Image.open(globalparam.auto_path+'/'+'result.jpg')  # 打开验证码图片
        # text_str = pytesseract.image_to_string(image, lang='eng').replace(" ", "")  # 识别图片中的字符串，strip()移除字符串头尾的空字符,replace(" ", "")移除所有空格
        code = ''.join(list(filter(str.isalnum, pytesseract.image_to_string(image, lang='eng').replace(" ", ""))))   # ''.join(list(filter(str.isalnum,str)))字符串过滤仅保留数字和字母
        # text = Tesseract.image_to_string('result.jpg', 'eng') # 通过Tesseract.py获取验证码字符串
        # code = ''.join(
        #     list(filter(str.isalnum, Tesseract.image_to_string('result.jpg', 'eng'))))  # 通过Tesseract.py获取验证码字符串
        # print(code)
        return code

    # 定义登录函数，将登录作为公共调用的模块，进行数据传递，因此不需要导入webdriver模块
    def login(self, username, password, code):
        try:
            driver = self.driver
            self.title = '易票联支付'  # 测试网站的Title
            assert self.title in driver.title
            # print(self.title)
            # print(driver.title)

            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(1) > div > div > input').clear()
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(1) > div > div > input').send_keys(username)  # 用户名
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(2) > div > div > input').clear()
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(2) > div > div > input').send_keys(password)  # 密码
            time.sleep(8)
            # driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(3) > div > div > div.ivu-col.ivu-col-span-17 > div > input').send_keys(code)  # 验证码
            #
            # wait = ui.WebDriverWait(driver, 5)
            #  # btn = driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > button > span')
            # btn = wait.until(lambda driver:driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/button'))
            # # print(btn)
            # time.sleep(2)
            # btn.click()
            # time.sleep(5)

        # 判断是否登录成功
            try:
                driver.find_element_by_css_selector('#app > div > div.main-header > div.logo-box > span')
                # admin_name = driver.find_element_by_css_selector('#app > div > div.main-header > div.logo-box > span').text    #获取网页元素值
                print("登录成功")
            except:
                print("登录失败")

        except StaleElementReferenceException:
            self.lgoin(self, username, password, code)
