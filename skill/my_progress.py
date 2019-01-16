#encoding=utf-8

import sys
import time
import random
import string
from requests import Request
import http.client
from urllib.parse import urlencode
from requests import Session

UA = 'mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) ' \
     'applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0 '
TIMEOUT = 10

# 生成指定位数的随机字符串，字符为字母或数字
def getRandomString(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = 'owzeBj'
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString

# 对指定的作品（zpid）投一张票

opid = getRandomString(22)
headers = {'Content-Type': 'text/html',
           'User-Agent': UA,
           'Connection': 'keep-alive',
           'Accept-Language': 'zh-CN,zh;q=0.9',
           }


class WeixinRequest(Request):
    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        Request.__init__(self, method, url, headers)

        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout

session = Session()
start_url = 'http://m.10pinping.com/v/p.php?s=a6290d47f9a18be1?goo36wy&from=groupmessage'
#weixin_request = Request(url=start_url)
req = Request('POST',url=start_url,headers=headers)
prepped = session.prepare_request(req)
r = session.send(prepped)
print(r.text)
