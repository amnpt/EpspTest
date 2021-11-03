# coding=utf-8

# 1、通过selenium获取验证码并识别，登录运营门户
# 2、通过pytesseract获取验证码并识别，登录运营门户

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
class login(unittest.TestCase):
    # setUp(self)设置初始化工作
    def setUp(self):
        self.driver = webdriver.Chrome()   # 创建Chrome浏览器驱动
        self.driver.implicitly_wait(15)   # 隐式等待一个命令完成，超过设置时间则抛出异常
        self.base_url = 'http://test-efps.epaylinks.cn/admin/#/login'  # 要测试的链接
        self.title = '易票联支付'  # 测试网站的Title
        # self.a_name = '运营管理系统'
        self.verificationErrors = []  # 定义空数组，脚本运行时的错误信息将被打印到这个数组中
        self.accept_next_alert = True  # 定义变量，表示是否继续接受下一个警告，初始化状态为True


    # 测试脚本
    def test_login(self):

        try:
            driver = self.driver
            driver.get(self.base_url)
            driver.maximize_window()
            driver.save_screenshot(globalparam.auto_path+'/'+'All.png')  # 截取当前网页，该网页有我们需要的验证码
            imgelement = driver.find_element_by_class_name('code-img')

            location = imgelement.location  # 获取验证码x,y轴坐标
            size = imgelement.size  # 获取验证码的长宽
            rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                      int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
            # i = Image.open("G:/8.python/pytest_testApi/file/All.png")  # 打开截图
            i = Image.open(globalparam.auto_path+'/'+'All.png')  # 打开截图
            result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
            result = result.convert('RGB')   # RGBA意思是红色，绿色，蓝色，Alpha的色彩空间，Alpha指透明度。而JPG不支持透明度，所以要么丢弃Alpha,要么保存为.png文件
            result_size = result.resize((140, 80))
            result_size.save(globalparam.auto_path+'/'+'result.jpg')   # 保存验证码图片
            time.sleep(3)
            image = Image.open(globalparam.auto_path+'/'+'result.jpg')  # 打开验证码图片
            # text_str = pytesseract.image_to_string(image, lang='eng').replace(" ", "")  # 识别图片中的字符串，strip()移除字符串头尾的空字符,replace(" ", "")移除所有空格
            text = ''.join(list(filter(str.isalnum, pytesseract.image_to_string(image, lang='eng').replace(" ", ""))))   # ''.join(list(filter(str.isalnum,str)))字符串过滤仅保留数字和字母
            # text = Tesseract.image_to_string('result.jpg', 'eng') # 通过Tesseract.py获取验证码字符串
            # text = ''.join(list(filter(str.isalnum,Tesseract.image_to_string(image, 'eng'))))  # 通过Tesseract.py获取验证码字符串
            print(text)

            assert self.title in driver.title
            # print(self.title)
            # print(driver.title)

            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(1) > div > div > input').clear()
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(1) > div > div > input').send_keys('zhengyanqin')  # 用户名
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(2) > div > div > input').clear()
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(2) > div > div > input').send_keys('KVTW1P')  # 密码
            driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-body > form > div:nth-child(3) > div > div > div.ivu-col.ivu-col-span-17 > div > input').send_keys(text)  # 验证码

            wait = ui.WebDriverWait(driver, 5)
            # btn = driver.find_element_by_css_selector('body > div.login-modal.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > button > span')
            btn = wait.until(lambda driver:driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/button'))
            # print(btn)
            time.sleep(2)
            btn.click()
            time.sleep(3)

            # 判断是否登录成功
            try:
                driver.find_element_by_css_selector('#app > div > div.main-header > div.logo-box > span')
                # admin_name = driver.find_element_by_css_selector('#app > div > div.main-header > div.logo-box > span').text    #获取网页元素值
                print("登录成功")
            except:
                print("登录失败")

        except StaleElementReferenceException:
            self.test_lgoin(self)

    # 处理查找页面元素是否存在
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)  #接收元素的定位方式（how）和定位值（what），如果定位到元素返回True，否则出现异常并返回Flase
        except NoSuchElementException as e:
            return False
        return True

    # 处理弹出的警告框
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()  # 捕捉警告框，如果捕捉到警告框返回True，否则异常，返回Flase
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭警告并且获得警告信息
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()  # 捕获警告
            alert_text = alert.text  # 获得警告框信息
            if self.accept_next_alert:  # 判断accept_next_alert状态，如果为True,通过accept()接受警告，否则dismiss()
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    # 用于完成测试用例执行后的清理工作，如退出浏览器、关闭驱动，恢复用例执行状态等。在每个测试方法执行后调用
    def tearDown(self):
        # self.driver.quit()
        self.assertEqual([], self.verificationErrors)  # 判断verificationErrors是否为空，如果为空说明用例执行的过程没有出现异常，否则抛出AssertionError 异常


# if __name__ == "__main__":
#     unittest.main()