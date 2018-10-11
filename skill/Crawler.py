https://github.com/Python3WebSpider/GithubLogin #模拟登录
https://blog.csdn.net/qq_21180877/article/details/79137699 #实战之解析

 
# 模拟点击登录
browser.find_element_by_xpath("//*[@class='btn btn-lg btn-block btn-signin']").click()

# 等待3秒
time.sleep(3)
url = "http://yun.zjnad.com/csc/abn-log/index?username=&dayS=2018-09-01&dayE=2018-09-30&danger=0&state=0&opt=search&codex="
browser.get(url)

#获取cookie
browser.get_cookies()
#保存 cookie
cookies_db.set(username,json.dumps(cookies))

time.sleep(1)
wb_data = requests.get(url)
#print(wb_data) #登录不成功 说明没有记录cookie或者别的方法试试
soup = BeautifulSoup(wb_data.text,'lxml') #lxml HTML解析器 用"html.parser"是Python的标准库
print(soup.prettify())
