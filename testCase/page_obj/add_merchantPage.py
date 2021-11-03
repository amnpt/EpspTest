# coding=utf-8
# 获取元素定位及进行元素操作

import time
import os
from data.data_opera import data_Op
from common.base import Page
from testCase.page_obj.element_opera import element_Op
data1 = data_Op().get_data(sheet="addMerchant")

class addMerchant(Page):
    # 定位器
    # 1、属性信息
    # 角色，勾选框（默认值）
    # 平台商户，输入查询
    platcustomercode_loc1 = ("css selector", "#time00 > div:nth-child(4) > div > div > div:nth-child(1) > div > input")
    platcustomercode_loc2 = ("css selector", "#time00 > div:nth-child(4) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li")
    def a1_platcustomercode(self, platcustomer_code):
        element_Op(self.driver).input_find(self.platcustomercode_loc1, platcustomer_code, self.platcustomercode_loc2)


    # 代理商户，输入查询
    sercustomercode_loc1 = ("css selector", "#time00 > div:nth-child(5) > div > div > div:nth-child(1) > div > input")
    sercustomercode_loc2 = ("css selector", "#time00 > div:nth-child(5) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li")
    def a1_sercustomercode(self, sercustomer_code):
        element_Op(self.driver).input_find(self.sercustomercode_loc1, sercustomer_code, self.sercustomercode_loc2)

    # 分组（平台商户），勾选框
    group_loc1 = ("css selector", "#time00 > div:nth-child(7) > div > div > label")
    def a1_group(self):
        self.click(self.group_loc1)

    # 分组（普通商户），下拉选择
    group_loc2 = ("css selector", "#time00 > div:nth-child(6) > div > div > div.ivu-select-selection > div > span")
    group_loc3 = ("css selector", "#time00 > div:nth-child(6) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li")
    def a2_group(self):
        element_Op(self.driver).drow_box(self.group_loc2, self.group_loc3)

    # 性质，下拉框（使用默认值）
    # 预算分组，下拉框
    budgetgroup_loc1 = ("css selector", "#time00 > div:nth-child(9) > div > div > div.ivu-select-selection > div > span")
    budgetgroup_loc2 = ("css selector", "#time00 > div:nth-child(9) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(2)")
    def a1_budgetgroup(self):
        element_Op(self.driver).drow_box(self.budgetgroup_loc1, self.budgetgroup_loc2)
        # self.click(self.budgetgroup_loc1)
        # time.sleep(1)
        # element_Op(self.driver).el_nocover(self.budgetgroup_loc2)

    # 2、联系信息
    # 联系人姓名，输入框
    contacts_loc1 = ("css selector", "#time01 > div.process-add-cell.ivu-form-item.ivu-form-item-required > div > div > input")
    def a1_contacts(self, contacts1):
        element_Op(self.driver).scroll_intoView(self.contacts_loc1)
        self.clear_type(self.contacts_loc1, contacts1)

    # 手机号码，输入框
    mobile_loc1 = ("css selector", "#time01 > div:nth-child(3) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input")
    def a1_mobile(self, mobile1):
        self.clear_type(self.mobile_loc1, mobile1)

    # 联系邮箱，输入框
    email_loc1 = ("css selector", "#time01 > div:nth-child(4) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input")
    def a1_email(self, email1):
        self.clear_type(self.email_loc1, email1)


    # 业务员，输入框
    businessman_loc1 = ("css selector", "#time01 > div:nth-child(5) > div > div > div:nth-child(1) > div > input")
    def a1_businessman(self, business_man):
        # driver.execute_script("arguments[0].scrollIntoView();", self.businessman_loc1)
        self.clear_type(self.businessman_loc1, business_man)

    # 3、基本信息
    # 商户简称，输入框
    shortname_loc1 = ("css selector", "#time02 > div.process-add-outer > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input")
    def a1_shortname(self, short_name):
        element_Op(self.driver).scroll_intoView(self.shortname_loc1)
        self.clear_type(self.shortname_loc1, short_name)

    # 客服电话，输入框
    phone_loc1 = ("css selector", "#time02 > div:nth-child(3) > div > div > input")
    def a1_phone(self, phone1):
        self.clear_type(self.phone_loc1, phone1)

    # 商户类型，多个下拉框
    custtype_loc1 = ("css selector", "#time02 > div:nth-child(4) > div > div > div:nth-child(1) > div > div.ivu-select-selection > div > span")
    custtype_loc2 = ("css selector", "#time02 > div:nth-child(4) > div > div > div:nth-child(1) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(1)")
    custtype_loc3 = ("css selector", "#time02 > div.process-add-cell.ivu-form-item.ivu-form-item-required.ivu-form-item-error > div > div.ivu-row > div:nth-child(2) > div > div.ivu-select-selection > div > span")
    custtype_loc4 = ("css selector", "#time02 > div.process-add-cell.ivu-form-item.ivu-form-item-required.ivu-form-item-error > div > div.ivu-row > div:nth-child(2) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(4)")

    def a1_custtype(self):
        element_Op(self.driver).drow_box(self.custtype_loc1, self.custtype_loc2)   # 第一个下拉框
        time.sleep(1)
        element_Op(self.driver).drow_box(self.custtype_loc3, self.custtype_loc4)   # 第二个下拉框

    # 经营地址，多个下拉框+输入框
    busaddress_loc1 = ("css selector", "#time02 > div:nth-child(5) > div > div > div:nth-child(1) > div > div.ivu-select-selection > div > span")
    busaddress_loc2 = ("css selector", "#time02 > div:nth-child(5) > div > div > div:nth-child(1) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(19)")
    busaddress_loc3 = ("css selector", "#time02 > div:nth-child(5) > div > div > div:nth-child(2) > div > div.ivu-select-selection > div > span")
    busaddress_loc4 = ("css selector", "#time02 > div:nth-child(5) > div > div > div:nth-child(2) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(21)")
    busaddress_loc5 = ("css selector", "#time02 > div:nth-child(5) > div > div > div:nth-child(3) > div > div.ivu-select-selection > div > span")
    busaddress_loc6 = ("css selector", "#time02 > div:nth-child(5) > div > div > div:nth-child(3) > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(6)")
    busaddress_loc7 = ("css selector", "#time02 > div:nth-child(6) > div > div > input")
    def a1_busaddress(self, bus_address):
        eop = element_Op(self.driver)
        eop.drow_box(self.busaddress_loc1, self.busaddress_loc2)   # 第一个下拉框
        time.sleep(1)
        eop.drow_box(self.busaddress_loc3, self.busaddress_loc4)   # 第二个下拉框
        time.sleep(1)
        eop.drow_box(self.busaddress_loc5, self.busaddress_loc6)   # 第三个下拉框
        self.clear_type(self.busaddress_loc7, bus_address)   # 输入框


    # 经营场所照片，上传照片
    busphoto_loc1 = ("css selector", "#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(1) > div")
    busphoto_loc2 = ("css selector", "#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(2) > div")
    busphoto_loc3 = ("css selector", "#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(3) > div")
    busphoto_loc4 = ("css selector", "#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(4) > div")
    busphoto_loc5 = ("css selector", "#time02 > div:nth-child(7) > div > div.ivu-row > div:nth-child(5) > div")
    bphoto_lis = [busphoto_loc1, busphoto_loc2, busphoto_loc3, busphoto_loc4, busphoto_loc5]

    def a1_busphoto(self, up_photo):
        element_Op(self.driver).up_file(self.bphoto_lis, up_photo)

    # 其他附件（选填），上传照片
    otherphoto_loc1 = ("css selector", "#time02 > div:nth-child(8) > div > div > div:nth-child(1) > div")
    otherphoto_loc2 = ("css selector", "#time02 > div:nth-child(8) > div > div > div:nth-child(2) > div")
    otherphoto_loc3 = ("css selector", "#time02 > div:nth-child(8) > div > div > div:nth-child(3) > div")
    otherphoto_loc4 = ("css selector", "#time02 > div:nth-child(8) > div > div > div:nth-child(4) > div")
    otherphoto_loc5 = ("css selector", "#time02 > div:nth-child(8) > div > div > div:nth-child(5) > div")
    ophoto_lis = [otherphoto_loc1, otherphoto_loc2, otherphoto_loc3, otherphoto_loc4, otherphoto_loc5]

    def a1_otherphoto(self, up_photo):
        element_Op(self.driver).up_file(self.ophoto_lis, up_photo)

    # ZIP附件（选填），上传zip文件
    zipfile_loc1 = ("css selector", "#time02 > div:nth-child(9) > div > div > div > div > div")
    zfile_lis = [zipfile_loc1]
    def a1_zipfile(self, up_file):
        element_Op(self.driver).up_file(self.zfile_lis, up_file)

    # 4、营业执照
    # 营业执照类型，勾选框（使用默认）
    # 营业执照照片，上传照片
    buslicphoto_loc1 = ("css selector", "#time03 > div:nth-child(3) > div > div.merchant-detail-attach.process-add-file > div > div.merchant-upload-box.ivu-upload > div > div")
    licphoto_lis = [buslicphoto_loc1]
    def a1_buslicphoto(self, up_photo):
        element_Op(self.driver).scroll_intoView(self.buslicphoto_loc1)
        element_Op(self.driver).up_file(self.licphoto_lis, up_photo)

    # 注册号，输入框
    buslicno_loc1 = ("css selector", "#time03 > div.process-add-col.process-add-outer > div > div > div > input")
    def a1_buslicno(self, buslic_no):
        self.clear_type(self.buslicno_loc1, buslic_no)

    # 商户名称，输入框
    customername_loc1 = ("css selector", "#time03 > div:nth-child(5) > div.process-add-cell.fl.ivu-form-item.ivu-form-item-required > div > div > input")
    def a1_customername(self, customer_name):
        self.clear_type(self.customername_loc1, customer_name)

    # 注册地址，输入框
    regaddress_loc1 = ("css selector", "#time03 > div:nth-child(6) > div > div > input")
    def a1_regaddress(self, reg_address):
        self.clear_type(self.regaddress_loc1, reg_address)

    # 营业期限，日期控件（用id获取）
    busdtime_loc1 = ("id", "businessLicenseFrom")
    busdtime_loc2 = ("css selector", "#businessLicenseFrom > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span.ivu-date-picker-cells-cell.ivu-date-picker-cells-cell-today.ivu-date-picker-cells-focused")
    busdtime_loc3 = ("id", "businessLicenseTo")
    busdtime_loc4 = ("css selector", "#businessLicenseTo > div.ivu-select-dropdown > div > div > div > div.ivu-date-picker-header > span.ivu-picker-panel-icon-btn.ivu-date-picker-next-btn.ivu-date-picker-next-btn-arrow-double")
    busdtime_loc5 = ("css selector", "#businessLicenseTo > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span:nth-child(33)")

    def a1_busdtime(self):
        element_Op(self.driver).date_time(self.busdtime_loc1, self.busdtime_loc2, self.busdtime_loc3, self.busdtime_loc4, self.busdtime_loc5)
        # self.click(self.busdtime_loc1)
        # element_Op(self.driver).el_nocover(self.busdtime_loc2)
        # self.click(self.busdtime_loc3)
        # self.double_click(self.busdtime_loc4)
        # element_Op(self.driver).el_nocover(self.busdtime_loc5)

    # 经营范围，输入框
    buscope_loc1 = ("css selector", "#time03 > div:nth-child(8) > div > div.ivu-input-wrapper.ivu-input-type > input")
    def a1_busscope(self, bus_scope):
        self.clear_type(self.buscope_loc1, bus_scope)

    # 法定代表人，输入框
    leapername_loc1 = ("css selector", "#time03 > div:nth-child(9) > div > div.ivu-input-wrapper.ivu-input-type > input")
    def a1_leapername(self, leaper_name):
        self.clear_type(self.leapername_loc1, leaper_name)

    # 5、法人证件
    # 身份证人像面照片/身份证国徽面照片，上传照片
    denphoto_loc1 = ("css selector", "#time04 > div:nth-child(2) > div > div > div.merchant-detail-attach.process-add-file > div > div.merchant-upload-box.ivu-upload > div > div")
    denphoto_loc2 = ("css selector", "#time04 > div:nth-child(3) > div > div > div.merchant-detail-attach.process-add-file > div > div.merchant-upload-box.ivu-upload > div > div")
    dphoto_lis = [denphoto_loc1, denphoto_loc2]
    def a1_denphoto(self, up_phdoto):
        element_Op(self.driver).scroll_intoView(self.denphoto_loc1)
        element_Op(self.driver).up_file(self.dphoto_lis, up_phdoto)

    # 证件类型，下拉框（默认值）
    # 证件号码，输入框
    leaperdeno_loc1 = ("css selector", "#time04 > div:nth-child(5) > div > div > input")
    def a1_leaperdeno(self, leaperde_no):
        self.clear_type(self.leaperdeno_loc1, leaperde_no)

    # 证件人姓名，输入框
    leaperdename_loc1 = ("css selector", "#time04 > div:nth-child(6) > div > div > input")
    def a1_leaperdename(self, leaperde_name):
        self.clear_type(self.leaperdename_loc1, leaperde_name)

    # 证件有效期，日期控件
    leadtime_loc1 = ("id", "certificateFrom")
    leadtime_loc2 = ("css selector", "#certificateFrom > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span.ivu-date-picker-cells-cell.ivu-date-picker-cells-cell-today.ivu-date-picker-cells-focused")
    leadtime_loc3 = ("id", "certificateTo")
    leadtime_loc4 = ("css selector", "#certificateTo > div.ivu-select-dropdown > div > div > div > div.ivu-date-picker-header > span.ivu-picker-panel-icon-btn.ivu-date-picker-next-btn.ivu-date-picker-next-btn-arrow-double")
    leadtime_loc5 = ("css selector", "#certificateTo > div.ivu-select-dropdown > div > div > div > div:nth-child(2) > div > span:nth-child(36)")
    def a1_leadtime(self):
        element_Op(self.driver).date_time(self.leadtime_loc1, self.leadtime_loc2, self.leadtime_loc3, self.leadtime_loc4, self.leadtime_loc5)

    # 6、实际控制人（选填）
    # 7、对公账户信息
    # 证明文件（选填）
    # 开户名称，只读
    pubcname_loc1 = ("css selector", "#time06 > div:nth-child(3) > div > div")
    def a1_pubcname(self):
        element_Op(self.driver).scroll_intoView(self.pubcname_loc1)

    # 银行账号，输入框
    pubankcard_loc1 = ("css selector", "#time06 > div:nth-child(4) > div > div > input")
    def a1_pubankcard(self, pu_bankcard):
        self.clear_type(self.pubankcard_loc1, pu_bankcard)

    # 开户银行，输入框（自动识别）
    # 开户支行，输入查询
    pubranch_loc1 = ("css selector", "#time06 > div:nth-child(6) > div > div > div:nth-child(1) > div > input")
    pubranch_loc2 = ("css selector", "#time06 > div:nth-child(6) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li")
    def a1_pubranch(self, pu_branch):
        element_Op(self.driver).input_find(self.pubranch_loc1, pu_branch, self.pubranch_loc2)

    # 8、结算账户
    # 账户类型，下拉框
    settbctype_loc1 = ("css selector", "#time07 > div:nth-child(2) > div > div > div.ivu-select-selection > div > span")
    settbctype_loc2 = ("css selector", "#time07 > div:nth-child(2) > div > div > div.ivu-select-dropdown > ul.ivu-select-dropdown-list > li:nth-child(2)")
    def a1_settbctype(self):
        element_Op(self.driver).scroll_intoView(self.settbranch_loc1)
        element_Op(self.driver).drow_box(self.settbctype_loc1, self.settbctype_loc2)

    # 银行卡照片（选填）
    # 开户名称，只读
    # 银行账户，输入框
    settbankcard_loc1 = ("css selector", "#time07 > div:nth-child(5) > div > div > input")
    def a1_settbankcard(self, sett_bankcard):
        self.clear_type(self.settbankcard_loc1, sett_bankcard)

    # 开户银行，输入框（自动识别）
    # 开户支行，输入查询
    settbranch_loc1 = ("css selector", "#time07 > div:nth-child(7) > div > div > div:nth-child(1) > div > input")
    settbranch_loc2 = ("css selector", "#time07 > div:nth-child(7) > div > div > div.ivu-select-dropdown.ivu-auto-complete > ul.ivu-select-dropdown-list > li")
    def a1_settbranch(self, sett_branch):
        element_Op(self.driver).input_find(self.settbranch_loc1, sett_branch, self.settbranch_loc2)

    # 联行号，自动带出
    # 附件
    bankcardfile_loc1 = ("css selector", "#time07 > div:nth-child(9) > div > div > div > button > i")
    bcfile_lis = [bankcardfile_loc1]
    def a1_bcardfile(self, up_file):
        element_Op(self.driver).up_file(self.bcfile_lis, up_file)

    # 8、更多信息（选填）
    # 银联简称，输入框
    unshortname_loc1 = ("css selector", "#time08 > div:nth-child(11) > div > div > input")
    def a1_unshortname(self, un_shortname):
        element_Op(self.driver).scroll_intoView(self.unshortname_loc1)
        self.clear_type(self.unshortname_loc1, un_shortname)

    # 备注，输入框
    remark_loc1 = ("css selector", "#time08 > div:nth-child(12) > div > div > textarea")
    def a1_remark(self, remark1):
        self.clear_type(self.remark_loc1, remark1)

    # 9、按钮操作
    # 提交审核
    subreview_loc = ("#stickerCon > div.main-container-box > div > div.process-add-box > div > button:nth-child(1) > span")
    def op1_subreview(self):
        self.click(self.subreview_loc)

    # 保存草稿
    savedraft_loc = ("css selector", "#stickerCon > div.main-container-box > div > div.process-add-box > div > button:nth-child(2) > span")
    def op1_savedraft(self):
        self.click(self.savedraft_loc)

    # 返回
    return_loc = ("css selector", "#stickerCon > div.main-container-box > div > div.process-add-box > div > button:nth-child(3) > span")
    def op1_return(self):
        self.click(self.return_loc)

    # 组合输入
    def all_insert1(self, platcustomer_code, sercustomer_code, contacts1, mobile1, email1, business_man, short_name,
                   phone1, bus_address, up_photo, up_file, buslic_no, customer_name, reg_address, bus_scope, leaper_name,
                   leaperde_no, leaperde_name, pu_bankcard, pu_branch, sett_bankcard, sett_branch, un_shortname, remark1):
        pass

    def all_insert(self, platcustomer_code = data1[0]['platcustomercode'], sercustomer_code = data1[0]['sercustomercode'],
                       contacts1 = data1[0]['contacts'], mobile1 = data1[0]['mobile'], email1 = data1[0]['email'],
                   business_man = data1[0]['businessman'], short_name = data1[0]['shortname'], phone1 = data1[0]['phone'],
                   bus_address = data1[0]['busaddress'], up_photo=data1[0]['busphoto'], up_file=data1[0]['zipfile'],
                   buslic_no=data1[0]['buslicenseno'], customer_name=data1[0]['customername'],
                   reg_address=data1[0]['registaddress'], bus_scope=data1[0]['busscope'], leaper_name=data1[0]['leapername'],
                   leaperde_no=data1[0]['leaperdeno'], leaperde_name=data1[0]['leaperdename'],
                   pu_bankcard=data1[0]['pubankcard'], pu_branch=data1[0]['pubranch'],
                   sett_bankcard=data1[0]['settbankcard'], sett_branch=data1[0]['settbranch'],
                   un_shortname=data1[0]['unionshortname'], remark1=data1[0]['remark']):

        # self.a1_platcustomercode(platcustomer_code)
        # self.a1_sercustomercode(sercustomer_code)
        # self.a2_group()
        # self.a1_budgetgroup()
        # self.a1_contacts(contacts1)
        self.a1_mobile(mobile1)
        self.a1_email(email1)
        # self.a1_businessman(business_man)
        # self.a1_shortname(short_name)
        # self.a1_phone(phone1)
        # self.a1_custtype()
        # self.a1_busaddress(bus_address)
        # self.a1_busphoto(up_photo)
        # self.a1_zipfile(up_file)
        # self.a1_buslicphoto(up_photo)
        # self.a1_buslicno(buslic_no)
        # self.a1_customername(customer_name)
        # self.a1_regaddress(reg_address)
        # self.a1_busdtime()
        # self.a1_busscope(bus_scope)
        # self.a1_leapername(leaper_name)
        # self.a1_denphoto(up_photo)
        # self.a1_leaperdeno(leaperde_no)
        # self.a1_leaperdename(leaperde_name)
        # self.a1_leadtime()
        # self.a1_pubcname()    # 只读字段，展示在可视区域
        # self.a1_pubankcard(pu_bankcard)
        # self.a1_pubranch(pu_branch)
        # self.a1_settbctype()
        # self.a1_settbankcard(sett_bankcard)
        # self.a1_settbranch(sett_branch)
        # self.a1_bcardfile(up_file)
        # self.a1_unshortname(un_shortname)
        # self.a1_remark(remark1)
        # time.sleep(3)
        # self.op1_return()



    # 定位器
    input_error_loc = ("class name", "wrong")
    add_merchant_success_loc = ("css selector", "span[title = '测试']")
    # Action
    def add_merchant_error_hint(self,actual):
        """平台商户不存在"""
        return self.is_text_in_element(self.input_error_loc, actual)
    def add_merchant_success(self,actual):
        """成功获取到平台商户"""
        return self.is_text_in_element(self.add_merchant_success_loc, actual)