# coding=utf-8

from config import globalparam
from common.base import Page

def insert_img(driver, file_name):
    """Screenshot function"""
    file_path = globalparam.img_path + "\\" + file_name
    Page(driver).take_screenshot(file_path)