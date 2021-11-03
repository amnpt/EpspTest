# coding=utf-8

# 通过selenium+pytesseract获取验证码图片
from selenium import webdriver
from PIL import Image
# import selenium.webdriver.support.ui as ui
# import unittest, time, re
import time
import pytesseract
from config import  globalparam

picture_file = globalparam.auto_path


# 继承unittest.TestCase类，从TestCase类继承是告诉unittest模式的方式，这是一个测试案例
class verify_Code():
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