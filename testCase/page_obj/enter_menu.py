# coding=utf-8
# 对进入操作页面流程进行封装
import time
from common.base import Page

class en_menu(Page):

    """
    进入测试页面
    """
    # 定位器
    # 进入新增商户页面（统一进件->商户管理->商户信息管理->新增）

    unifiedInput_loc = ("css selector", "#app > div > div.main-header > div.header-inner > div.header-menu > ul > li:nth-child(9)")
    merchantManage_loc = ("css selector", "#app > div > div.main-wrapper > div.side-wrapper.light > div > div > ul > div:nth-child(1) > li > ul > li:nth-child(2)")
    addMerchant_loc = ("css selector", "#stickerCon > div.main-container-box > div > div > div:nth-child(2) > div > div > button:nth-child(1)")

    def enter_Merchant(self):
        self.click(self.unifiedInput_loc)
        self.click(self.merchantManage_loc)

    def enter_addMerchant(self):
        self.click(self.addMerchant_loc)


    # 进入新增报备卡页面（账户管理-银行账户管理-银行账户）
    accManage_loc = ("css selector", "#app > div > div.main-header > div.header-inner > div.header-menu > ul > li:nth-child(2)")
    bankAccManage_loc = ("css selector", "#app > div > div.main-wrapper > div.side-wrapper.light > div > div > ul > div:nth-child(3) > li")
    bankAcc_loc = ("css selector", "#app > div > div.main-wrapper > div.side-wrapper.light > div > div > ul > div:nth-child(3) > li > ul")
    addBankAcc_loc = ("css selector", "#stickerCon > div.main-container-box > div > div:nth-child(2) > div > div > button:nth-child(1)")

    def enter_addBankcard(self):
        self.click(self.accManage_loc)
        self.click(self.bankAccManage_loc)
        self.click(self.bankAcc_loc)
        self.click(self.addBankAcc_loc)