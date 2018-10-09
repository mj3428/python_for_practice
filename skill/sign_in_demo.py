#!/usr/bin/env python
# encoding: utf-8
'''
@author: miaojue
@contact: major3428@foxmail.com
@software: pycharm
@file: crawler_zjnad2.py
@time: 2018-10-9 上午 11:28
@desc:
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

########模拟登录可行
browser = webdriver.Chrome()
browser.get("http://yun.zjnad.com/csc/public/login")

# 输入账号密码
browser.find_element_by_name("Csc[mob]").send_keys("18505816789")
browser.find_element_by_name("Csc[password]").send_keys("22222222")

# 模拟点击登录
try:
    browser.find_element_by_xpath("//*[@class='btn btn-lg btn-block btn-signin']").click()
    print ('click success!')
except:
    print('click error!')
# 等待3秒
time.sleep(3)

# 生成登陆后快照 #运行成功
#browser.save_screenshot("zjnad.png")

if __name__ == '__main__':
