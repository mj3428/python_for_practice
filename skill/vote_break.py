#!/usr/bin/env python
# encoding: utf-8
'''
@author: miaojue
@contact: major3428@foxmail.com
@software: pycharm
@file: test7.py
@time: 2019-1-15 上午 8:54
@desc:
'''

import random
import hashlib
ex = random.randint(40000, 59999)

queryString = 'rnd=48689448809' + str(ex) + '&authType=10&id=448809'
strs = queryString.split("&")
print(strs)
strs.sort()
vals = ''
for i in range(len(strs)):
    vals = vals+strs[i].split("=")[1]
print(vals)
m2 = hashlib.md5()
m2.update(str(vals).encode('utf-8'))
hex_md5 = m2.hexdigest()
print(ex)
new_url = 'http://v.10pinping.com/api/captcha.check.2.php' \
          '?rnd=48689448809' + str(ex) +'&authType=10&id=448809&sign=' + hex_md5
print(new_url)

