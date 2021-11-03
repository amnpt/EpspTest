# coding=utf-8
import unittest
from common.Log import loggerClass
from common.base import Page
from common import browser
from config import globalparam
from selenium import webdriver

class MyTest(unittest.TestCase, Page):

    @classmethod
    def setUpClass(self):
        self.logger = loggerClass()
        self.logger.info('############################### START ###############################')
        self.driver = browser.select_browser(globalparam.browser)
        self.driver.implicitly_wait(10)
        Page(self.driver).max_window()


    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')
