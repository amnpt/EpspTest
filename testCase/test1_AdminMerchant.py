# coding=utf-8

# 门户进件
import os
# from runtime import runtime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
from common import get_Config
from common.login.Login_go import Loginfor

class AdminMerchant(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(get_Config.get_admin_Url())
        self.driver.implicitly_wait(15)

    def test_AdminMerchant(self):
        code = Loginfor(self.driver).get_code()
        print(code)
        Loginfor(self.driver).login(get_Config.get_admin_Username(), get_Config.get_admin_Password(), code)
        time.sleep(3)

# 统一进件

        # 进入 商户信息管理 页面
        # try:
        self.driver.find_element_by_css_selector('#app > div > div.main-header > div.header-inner > div.header-menu > ul > li:nth-child(9)').click()
            # self.driver.find_elements_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div[2]/ul/li[9]').click()
        time.sleep(2)

        self.driver.find_element_by_css_selector('#app > div > div.main-wrapper > div.side-wrapper.light > div > div > ul > div:nth-child(1) > li > ul > li:nth-child(2)').click()
        time.sleep(2)
        # 点击【新增】，进入 新增商户 页面
        self.driver.find_element_by_css_selector('#stickerCon > div.main-container-box > div > div > div:nth-child(2) > div > div > button:nth-child(1)').click()
        print("开始新增普通商户信息")
        # 新增平台商户信息
        time.sleep(2)

        #属性信息
        # 1、角色，勾选框（默认值）
        # self.driver.find_element_by_css_selector('#time00 > div.process-add-outer > div.process-add-cell.fl.ivu-form-item > div > div > label:nth-child(2) > span:nth-child(2)').click()
        # time.sleep(2)
        # 2、平台商户，输入查询
        element1_0 = self.driver.find_element_by_css_selector('#time00 > div:nth-child(4) > div > div > div:nth-child(1) > div > input')
        element1_0.send_keys('5651200003063343')
        element1_0.click()
        time.sleep(1)
        self.driver.find_element_by_css_selector('#time00 > div:nth-child(4) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li').click()
        time.sleep(1)

        # 2、所属代理商，输入查询
        # 1）定位元素->输入关键字
        # element2_0 = self.driver.find_element_by_css_selector('#time00 > div:nth-child(5) > div > div > div:nth-child(1) > div > input')
        # element2_0.send_keys("562505003079249")
        # # 2）点击查找
        # element2_0.click()
        # time.sleep(1)
        # # 3）选择下拉数据
        # self.driver.find_element_by_css_selector('#time00 > div:nth-child(5) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li').click()
        # time.sleep(1)
        # 3、分组,
        # 平台商户，勾选框
        # self.driver.find_element_by_css_selector('#time00 > div:nth-child(7) > div > div > label').click()
        # 普通商户，下拉选择
        self.driver.find_element_by_css_selector('#time00 > div:nth-child(6) > div > div > div.ivu-select-selection > div > span').click()
        self.driver.find_element_by_css_selector('#time00 > div:nth-child(6) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li').click()
        time.sleep(1)
        # 4、性质，下拉选择（有默认值“企业”，这里直接使用默认值）
        # 5、预算分组，下拉选择
        # 1）定位并点击输入框
        self.driver.find_element_by_css_selector('#time00 > div:nth-child(9) > div > div > div.ivu-select-selection > div > span').click()
        # 2）选择下拉数据
        time.sleep(1)
        element3_0 = self.driver.find_element_by_css_selector('#time00 > div:nth-child(9) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(2)')
        self.driver.execute_script("arguments[0].click();", element3_0)    # 下拉数据元素互相覆盖时，使用该方法可以正确找到元素并点击
        time.sleep(1)

        # 联系信息
        # 6、联系人姓名，输入框
        self.driver.find_element_by_css_selector('#time01 > div.process-add-cell.ivu-form-item.ivu-form-item-required > div > div > input').send_keys('郑小花')
        time.sleep(1)
        # 7、手机号码，输入框
        self.driver.find_element_by_css_selector('#time01 > div:nth-child(3) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input').send_keys('15989101463')
        time.sleep(1)
        # 8、联系邮箱，输入框
        self.driver.find_element_by_css_selector('#time01 > div:nth-child(4) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input').send_keys('zhengyanqin@epaylinks.cn')
        time.sleep(1)
        # 9、业务员，输入框
        self.driver.find_element_by_css_selector('#time01 > div:nth-child(5) > div > div > div:nth-child(1) > div > input').send_keys('郑小叶')
        time.sleep(1)

        # 基本信息
        # 10、商户简称，输入框
        self.driver.find_element_by_css_selector('#time02 > div.process-add-outer > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input').send_keys('郑小花第一店铺')
        time.sleep(1)
        # 11、客服电话，输入框
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(3) > div > div > input').send_keys('020-1234567')
        time.sleep(1)
        # 12、商户类别，多个下拉框
        # 1）第一个下拉框
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(4) > div > div > div:nth-child(1) > div > div.ivu-select-selection > div > span').click()
        element10_0 = self.driver.find_element_by_css_selector('#time02 > div:nth-child(4) > div > div > div:nth-child(1) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(1)')
        self.driver.execute_script("arguments[0].click();", element10_0)
        time.sleep(2)
        # 2)第二个下拉框
        self.driver.find_element_by_css_selector('#time02 > div.process-add-cell.ivu-form-item.ivu-form-item-required.ivu-form-item-error > div > div.ivu-row > div:nth-child(2) > div > div.ivu-select-selection > div > span').click()
        element10_1 = self.driver.find_element_by_css_selector('#time02 > div.process-add-cell.ivu-form-item.ivu-form-item-required.ivu-form-item-error > div > div.ivu-row > div:nth-child(2) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(4)')
        self.driver.execute_script("arguments[0].click();", element10_1)
        time.sleep(1)
        # 13、经营地址，多个下拉框+输入框
        # 1）第一个下拉框
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(5) > div > div > div:nth-child(1) > div > div.ivu-select-selection > div > span').click()
        element13_0 = self.driver.find_element_by_css_selector('#time02 > div:nth-child(5) > div > div > div:nth-child(1) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(19)')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element13_0)
        time.sleep(1)
        # 2）第二个下拉框
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(5) > div > div > div:nth-child(2) > div > div.ivu-select-selection > div > span').click()
        element13_1 = self.driver.find_element_by_css_selector('#time02 > div:nth-child(5) > div > div > div:nth-child(2) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(21)')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element13_1)
        time.sleep(1)
        # 3）第三个下拉框
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(5) > div > div > div:nth-child(3) > div > div.ivu-select-selection > div > span').click()
        element13_2 = self.driver.find_element_by_css_selector('#time02 > div:nth-child(5) > div > div > div:nth-child(3) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(6)')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element13_2)
        time.sleep(1)
        # 4）输入框
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(6) > div > div > input').send_keys('体育西横二街金穗路1001号')
        # 14、经营场所照片，上传照片
        # 1）第一张照片
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(1) > div > div > div.merchant-upload-box.ivu-upload > div').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')   # 调用可执行程序，调用系统上传功能
        time.sleep(3)
        # 2）第二张照片
        self.driver.find_element_by_css_selector(
            '#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(2) > div').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(2)
        # 3）第三张照片
        self.driver.find_element_by_css_selector(
            '#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(3) > div').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(2)
        # 4）第四张照片
        self.driver.find_element_by_css_selector(
            '#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(4) > div').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(2)
        # 5）第五张照片
        self.driver.find_element_by_css_selector(
            '#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(5) > div').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(3)
        # 15、其他附件（选填），上传照片
        element14_0 = self.driver.find_element_by_css_selector(
            '#time02 > div:nth-child(8) > div > div > div:nth-child(1) > div')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element14_0)   # 拉动滚动条，使控件展示在可视区域
        time.sleep(1)
        element14_0.click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(3)
        # 15、ZIP附件（选填），上传zip文件（元素找到了，点击不了，以下代码没生效，待解决）
        self.driver.find_element_by_css_selector('#time02 > div:nth-child(9) > div > div > div > div > div').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upZipfile.exe')
        time.sleep(3)
        # 营业执照
        # 16、营业执照类型，勾选框（使用默认）
        # 17、营业执照照片，上传照片
        self.driver.find_element_by_css_selector('#time03 > div:nth-child(3) > div > div.merchant-detail-attach.process-add-file > div > div.merchant-upload-box.ivu-upload > div > div').click()
        time.sleep(2)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element16_0)
        # element16_0.click()
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(3)
        # 18、注册号，输入框
        self.driver.find_element_by_css_selector('#time03 > div.process-add-col.process-add-outer > div > div > div > input').send_keys('111112222233333')
        time.sleep(1)
        # 19、商户名称，输入框
        self.driver.find_element_by_css_selector('#time03 > div:nth-child(5) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input').send_keys('郑小花广州第一店铺')
        time.sleep(2)
        # 20、注册地址，输入框(Exception: Message: no such element: Unable to locate element)
        self.driver.find_element_by_css_selector('#time03 > div:nth-child(6) > div > div > input').send_keys('广州市天河区体育西横二街金穗路1001号')
        time.sleep(1)
        # 21、营业期限，日期控件（用id获取）
        # 1） 开始时间
        self.driver.find_element_by_id('businessLicenseFrom').click()
        element21_0 = self.driver.find_element_by_css_selector(
            '#businessLicenseFrom > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span.ivu-date-picker-cells-cell.ivu-date-picker-cells-cell-today.ivu-date-picker-cells-focused')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element21_0)
        time.sleep(1)
        # 2） 结束时间
        self.driver.find_element_by_id('businessLicenseTo').click()
        time.sleep(1)
        element21_1 = self.driver.find_element_by_css_selector('#businessLicenseTo > div.ivu-select-dropdown > div > div > div > div.ivu-date-picker-header > span.ivu-picker-panel-icon-btn.ivu-date-picker-next-btn.ivu-date-picker-next-btn-arrow-double')
        time.sleep(1)
        element21_1.click()
        element21_1.click()
        time.sleep(1)
        element21_2 = self.driver.find_element_by_css_selector('#businessLicenseTo > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span:nth-child(33)')
        self.driver.execute_script("arguments[0].click();", element21_2)
        time.sleep(1)
        # 22、经营范围，输入框
        element22_0 = self.driver.find_element_by_css_selector('#time03 > div:nth-child(8) > div > div.ivu-input-wrapper.ivu-input-type > input')
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element22_0)  # 拉动滚动条，使控件展示在可视区域
        time.sleep(1)
        element22_0.send_keys('餐饮')
        time.sleep(1)
        # 23、法定代表人，输入框
        self.driver.find_element_by_css_selector('#time03 > div:nth-child(9) > div > div.ivu-input-wrapper.ivu-input-type > input').send_keys('郑小花')
        time.sleep(3)

        # 法人证件
        # 24、身份证人像面照片
        self.driver.find_element_by_css_selector(
            '#time04 > div:nth-child(2) > div > div > div.merchant-detail-attach.process-add-file > div > div.merchant-upload-box.ivu-upload > div > div').click()
        time.sleep(1)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element16_0)
        # element16_0.click()
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(3)
        # 25、身份证国徽面照片
        self.driver.find_element_by_css_selector(
            '#time04 > div:nth-child(3) > div > div > div.merchant-detail-attach.process-add-file > div > div.merchant-upload-box.ivu-upload > div > div').click()
        time.sleep(1)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element16_0)
        # element16_0.click()
        os.system('G:/8.python/pytest_testApi/file/upphoto.exe')
        time.sleep(5)
        # 26、证件类型，下拉框（默认值）
        # 27、证件号码，输入框
        self.driver.find_element_by_css_selector('#time04 > div:nth-child(5) > div > div > input').send_keys('441223202010261701')
        time.sleep(1)
        # 28、证件人姓名，输入框
        self.driver.find_element_by_css_selector('#time04 > div:nth-child(6) > div > div > input').send_keys('郑小花')
        time.sleep(1)
        # 29、证件有效期，日期控件（用id获取）
        # 1） 开始时间
        self.driver.find_element_by_id('certificateFrom').click()
        element29_0 = self.driver.find_element_by_css_selector(
            '#certificateFrom > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span.ivu-date-picker-cells-cell.ivu-date-picker-cells-cell-today.ivu-date-picker-cells-focused')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element29_0)
        time.sleep(1)
        # 2） 结束时间
        self.driver.find_element_by_id('certificateTo').click()
        time.sleep(1)
        element29_1 = self.driver.find_element_by_css_selector(
            '#certificateTo > div.ivu-select-dropdown > div > div > div > div.ivu-date-picker-header > span.ivu-picker-panel-icon-btn.ivu-date-picker-next-btn.ivu-date-picker-next-btn-arrow-double')
        time.sleep(1)
        element29_1.click()
        element29_1.click()
        time.sleep(1)
        element29_2 = self.driver.find_element_by_css_selector(
            '#certificateTo > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span:nth-child(36)')
        self.driver.execute_script("arguments[0].click();", element29_2)
        time.sleep(1)
        # 实际控制人（选填）
        # 30-33
        # 对公账户信息
        # 34、证明文件（选填）
        # 35、开户名称。只读
        # 36、银行账户，输入框
        element36_0 = self.driver.find_element_by_css_selector('#time06 > div:nth-child(4) > div > div > input')
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element36_0)
        time.sleep(1)
        element36_0.send_keys('6214850130561234')
        time.sleep(1)
        # 37、开户银行，输入框（自动识别）
        # 38、开户支行，输入查询
        element38_0 = self.driver.find_element_by_css_selector('#time06 > div:nth-child(6) > div > div > div:nth-child(1) > div > input')
        element38_0.send_keys('体育西')
        element38_0.click()
        element38_1 = self.driver.find_element_by_css_selector('#time06 > div:nth-child(6) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element38_1)
        time.sleep(1)

        # 结算账户
        # 39、账户类型，下拉选择
        self.driver.find_element_by_css_selector('#time07 > div:nth-child(2) > div > div > div.ivu-select-selection > div > span').click()
        element39_0 = self.driver.find_element_by_css_selector('#time07 > div:nth-child(2) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(2)')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element39_0)
        time.sleep(1)
        # 40、银行卡照片（选填）
        # 41、开户名称，只读
        # 42、银行账户，输入框
        element42_0 = self.driver.find_element_by_css_selector('#time07 > div:nth-child(5) > div > div > input')
        time.sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element42_0)
        time.sleep(1)
        element42_0.send_keys('6214850105364321')
        time.sleep(1)
        # 43、开户银行，输入框（自动识别）
        # 44、开户支行，输入查询
        element44_0 = self.driver.find_element_by_css_selector('#time07 > div:nth-child(7) > div > div > div:nth-child(1) > div > input')
        element44_0.send_keys('海珠')
        element44_0.click()
        element44_1 = self.driver.find_element_by_css_selector(
            '#time07 > div:nth-child(7) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li')
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", element44_1)
        time.sleep(1)
        # 45、联行号，自动带出
        # 46、附件
        self.driver.find_element_by_css_selector('#time07 > div:nth-child(9) > div > div > div > button > i').click()
        time.sleep(1)
        os.system('G:/8.python/pytest_testApi/file/upZipfile.exe')
        time.sleep(3)

        # 更新信息（选填）
        # 银联简称
        element00_0 = self.driver.find_element_by_css_selector('#time08 > div:nth-child(11) > div > div > input')
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element00_0)
        element00_0.send_keys('郑小花第一店铺')
        time.sleep(1)
        # 备注
        self.driver.find_element_by_css_selector('#time08 > div:nth-child(12) > div > div > textarea').send_keys('自动化测试')
        time.sleep(3)

        # 提交审核
        # self.driver.find_element_by_css_selector('#stickerCon > div.main-container-box > div > div.process-add-box > div > button:nth-child(1) > span').click()
        time.sleep(10)

        print('新增普通商户成功')

        # except:
        #     print("新增商户失败")
        #     self.driver.close()


   #新增报备卡

        # self.driver.find_element_by_css_selector('#app > div > div.main-header > div.header-inner > div.header-menu > ul > li:nth-child(2)').click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector('#app > div > div.main-wrapper > div.side-wrapper.light > div > div > ul > div:nth-child(3) > li').click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector('#app > div > div.main-wrapper > div.side-wrapper.light > div > div > ul > div:nth-child(3) > li > ul').click()
        # time.sleep(2)
        # self.driver.find_element_by_css_selector('#stickerCon > div.main-container-box > div > div:nth-child(2) > div > div > button:nth-child(1)').click()
        # print("开始新增报备卡")
        # time.sleep(10)

        # js_customer = "document.getElementsByClassName('ivu-input')[0]"
        # js_customer = "document.getElementsByClassName('ivu-input')[2].click();" \
        #      "document.getElementsByClassName('ivu-input')[2].value='5651200003063343'"
        #
        # self.driver.execute_script(js_customer)
        # self.driver.find_element_by_xpath("//*[@class='ivu-input']").send_keys("5651200003063343")
        # time.sleep(2)
        # s1 = Select(self.driver.find_element_by_class_name('ivu-select-selected-value'))
        # time.sleep(2)
        # s1.select_by_value('法人账户')
        # time.sleep(2)
        # self.driver.find_element_by_css_selector('#stickerCon > div.main-container-box > div > div:nth-child(1) > div > div > form > div:nth-child(2) > div:nth-child(2) > div > div > div > input').send_keys('郑小简')
        # time.sleep(2)
        # self.driver.find_element_by_css_selector('#stickerCon > div.main-container-box > div > div:nth-child(1) > div > div > form > div:nth-child(3) > div > div:nth-child(2) > div > div > div > input').send_keys('6214850100112233')
        # time.sleep(2)
        # self.driver.find_element_by_xpath("//*[@class='ivu-input']").send_keys("招商银行股份有限公司广州分行")

        # except:
        #     print("新增报备卡失败")
        #     self.driver.close()

    def tearDown(self):
        pass
