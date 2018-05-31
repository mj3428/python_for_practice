#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: download_data.py
@time: 2018-05-14 8:30
@desc:
'''

import datetime
import urllib.request

if __name__=="__main__":
    startdate=datetime.date(2018,5,12)
    enddate=datetime.date(2018,5,28)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    for i in range((enddate-startdate).days+1):
        if i%2==0:
            day1=startdate+datetime.timedelta(days=i)
            day2=startdate+datetime.timedelta(days=i+2)
            url="https://1token.trade/api/v1/quote/candles?contract=binance%2Fbtc.usdt&duration=15min&since="+str(day1)+"&until="+str(day2)
            #data=getUrlContent(url)
            req = urllib.request.Request(url, headers=headers)
            data=urllib.request.urlopen(req).read()

            #print(type(data))
            with open("e:/binancedata/"+str(day1)+"-"+str(day2)+".json", "wb+") as f:
            #a = json.dump(data, f)
                f.write(data)
                f.close()
