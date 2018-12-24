import csv
import re
import pymongo
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #可用于判断的条件
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from lxml import etree
import random


########模拟登录可行
browser = webdriver.Chrome()
browser.get("http://*********/public/login")

#添加智能等待
browser.implicitly_wait(20)
#设置等待10秒内,browser是driver的参数
wait = WebDriverWait(browser, 10)

# 输入账号密码
browser.find_element_by_name("解析出的账号名").send_keys("账号")
browser.find_element_by_name("解析出的密码").send_keys("密码")

# 模拟点击登录
try:
    browser.find_element_by_xpath("//*[@class='btn btn-lg btn-block btn-signin']").click()
    print ('click success!')
except:
    print('click error!')
# 等待3秒
time.sleep(3)

def get_head(html_source):
    html = etree.HTML(html_source)
    table_head = html.xpath("//table[@class='table table-striped table-hover']/thead/tr/th/text()")
    print(table_head)

def parse_page(html_source):
    html = etree.HTML(html_source) #html_source其实也是一个html格式文件
    table_data = html.xpath("//tbody[@id='log_list']/tr/td//text()")
    table_data = list(map(lambda x:x.replace(' ',""),table_data))

    for i in table_data[:]:
        result = re.match('\s*',i) #匹配所有换行符和无任何字符的字符串
        if i == result.group():
            table_data.remove(i)
    length = len(table_data)
    table_data = list(table_data[i:i+12] for i in range(0,length,12))
    #print (length)
    return table_data


# 生成登陆后快照 #运行成功
#browser.save_screenshot("zjnad.png")
url = "http://************page=1"

browser.get(url)

#在测试解析的时候如果出现gbk的字样的时候，我们可以通过在with open里加encoding='utf-8'来解决该问题

page_num = 0 #记录页数
#print (type(t_Data[0])) #返回list
while True:
    page_num += 1
    html_s = browser.page_source
    query = etree.HTML(html_s).xpath("//ul[@class='pagination']/li/@class")
    print('正在抓取第%d页' % page_num)
    # print(len(query)) #一直保持3个的大小
    print (query[-1])
    if query[-1] != 'next disabled':
        wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@class='pagination']/li/a")))
        t_Data = parse_page(html_s)
        with open('zjnad_data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)  # delimiter是控制分割符
            writer.writerows(t_Data)
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='pagination']/li[@class='next']/a[@data-page]")))
        time.sleep(random.uniform(1.2,6.6)) #最终发现确实是时间控制问题 最后一页会超时
        submit.click()
        #browser.find_element_by_xpath("//ul[@class='pagination']/li[@class='next']/a").click()
    else:
        t_Data = parse_page(html_s)
        with open('zjnad_data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)  # delimiter是控制分割符
            writer.writerows(t_Data)
        browser.close()
        break
    wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-striped table-hover']/tbody[@id='log_list']/tr")))

##大功告成
