# coding=utf-8
# 封装元素操作

import os
import time
from common.base import Page
from pymouse import PyMouse


class element_Op(Page):

    # 输入查询并选择
    def input_find(self, el1, send_key, el2):
        self.clear_type(el1, send_key)
        self.click(el1)
        time.sleep(2)
        self.click(el2)

    # 下拉框
    def drow_box(self, el1, el2):
        self.click(el1)
        time.sleep(1)
        self.js_view("arguments[0].click();", el2)

    # 下拉框防止元素定位相互覆盖
    def el_nocover(self, el):
       self.js_view("arguments[0].click();", el)

    # 拉动滚动条(元素与左上角顶部重合)
    def scroll_intoView(self, el):
        self.js_view("arguments[0].scrollIntoView();", el)

    # 上传文件(支持上传多个)
    def up_file(self, el_lis, filepath):
        for e in range(len(el_lis)):
            self.click(el_lis[e])
            e = e+1
            time.sleep(1)
            os.system(filepath)
            time.sleep(2)

    # 日期控件
    def date_time(self, el1, el2, el3, el4, el5):
        # 开始时间
        self.click(el1)
        self.el_nocover(el2)
        # 结束时间
        self.click(el3)
        self.double_click(el4)
        self.el_nocover(el5)

    # windows系统电脑鼠标指针移动、点击
    def win_mouse(self):
        m = PyMouse()
        tup = m.position()
        x = tup[0] + 5
        y = tup[1] - 5
        m.move(x, y)
        m.click(x, y, 1)    # 左击
        # m.click(x, y, 2)   # 右击




