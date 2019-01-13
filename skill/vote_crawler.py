from selenium import webdriver
import time
from urllib import request
import tesserocr
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #可用于判断的条件
from selenium.webdriver.support.wait import WebDriverWait

# 记录下载过的图片地址，避免重复下载
img_url_dic = {}
#解析图片的位置
pic = "//p[@class='body']/img"

WIDTH = 320
HEIGHT = 640
PIXEL_RATIO = 3.0
UA = 'mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0 '

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}

options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
# 设置代理
#options.add_argument("--proxy-server=http://202.20.16.82:10152")

browser = webdriver.Chrome(chrome_options=options)

# 查看本机ip，查看代理是否起作用
#browser.get("http://httpbin.org/ip")

browser.get('http://m.10pinping.com/v/p.php?s=a6290d47f9a18be1?goo36wy&from=groupmessage')
wait = WebDriverWait(browser, 10)
browser.find_element_by_xpath('//div[@class="stin_content"]/div[@class="stin_content_one"]/span[contains(@title, "日禾")]').click()

#browser.find_element_by_xpath('').click()

for element in browser.find_elements_by_xpath(pic):
    img_url = element.get_attribute('src')
    # 保存图片到指定路径
    if img_url != None and not img_url in img_url_dic:
        img_url_dic[img_url] = ''
        ext = img_url.split('.')[-2]
        filename = 'secret.' + ext
        data = request.urlopen(img_url).read()
        f = open('./' + filename, 'wb')
        f.write(data)
        f.close()
image = Image.open('./secret.png')

image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
#image.show()

result = tesserocr.image_to_text(image)
print(result)
browser.find_element_by_name("captcha").send_keys(result)

# 模拟点击登录
try:
    browser.find_element_by_xpath("//button[@class='vote_captcha_do']").click()
    print ('click success!')
except:
    print('click error!')

# 退出，清除浏览器缓存
browser.quit()
browser.close()
