https://github.com/Python3WebSpider/GithubLogin #模拟登录
https://blog.csdn.net/qq_21180877/article/details/79137699 #实战之解析

 
# 模拟点击登录
browser.find_element_by_xpath("//*[@class='btn btn-lg btn-block btn-signin']").click()

# 等待3秒
time.sleep(3)
url = "http://yun.zjnad.com/csc/abn-log/index?username=&dayS=2018-09-01&dayE=2018-09-30&danger=0&state=0&opt=search&codex=&page=1"
browser.get(url)

#获取cookie
browser.get_cookies()
#保存 cookie
cookies_db.set(username,json.dumps(cookies))

time.sleep(1)

cookies = '''
          
          '''
jar = requests.cookies.RequestsCookieJar()
for cookie in cookies.split(';'):
    key,value = cookie.split('=',1)
    jar.set(key,value)  #set方法设置好每个cookie的key和value
wb_data = requests.get(url,cookies=jar,headers=headers) #要写头部
print(wb_data.text)
#print(wb_data) #登录不成功 说明没有记录cookie或者别的方法试试
soup = BeautifulSoup(wb_data.text,'lxml') #lxml HTML解析器 用"html.parser"是Python的标准库
print(soup.prettify())

html = etree.parse('test.html',etree.HTMLParser()) #html_source其实也是一个html格式文件
table_head = html.xpath("//table[@class='table table-striped table-hover']/thead/tr/th/text()")
print (table_head)
table_data = html.xpath("//tbody[@id='log_list']/tr/td//text()")
table_data = list(map(lambda x:x.replace(' ',""),table_data))

for i in table_data[:]:
    result = re.match('\s*',i) #匹配所有换行符和无任何字符的字符串
    if i == result.group():
        table_data.remove(i)

table_data = list(table_data[i:i+12] for i in range(0,length,12)) #分割
#记得导入csv模块
with open('zjnad_data.csv','wb+') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table_data)
print (len(table_data))
print (table_data)
