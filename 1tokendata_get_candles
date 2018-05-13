import datetime
import urllib.request
import gzip
import json
'''
def getUrlContent(url):
    #返回页面内容
    doc = urllib.request.urlopen(url).read()
    #解码
    try:
        html=gzip.decompress(doc).decode("utf-8")
    except:
        html=doc.decode("utf-8")
    return html'''

if __name__=="__main__":
    startdate=datetime.date(2017,8,17)
    enddate=datetime.date(2018,5,9)
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
            with open("f:/btcdata/"+str(day1)+"-"+str(day2)+".txt", "wb+") as f:
            #a = json.dump(data, f)
                f.write(data)
                f.close()

            #print(data)
##################################
#下一步将所有的txt的内容放入一张txt中（暂时）
#然后将数据转换csv方便调用
import csv
import os
import pandas
import codecs
import glob
import pandas as pd
from pandas import DataFrame


os.getcwd()
os.chdir('f:/btcdata')

'''def txtcombine():

    files = glob.glob('*.txt')

    all = codecs.open('merge.txt','a')

    for filename in files:
        print(filename)
        fopen=codecs.open(filename,'r',encoding='utf-8')
        lines=[]
        lines=fopen.readlines()

        fopen.close()
        i=0
        for line in lines:
            for x in line:
                all.write(x)
        #读取为DataFrame格式
        #all1 = pd.read_csv('all.txt',sep=' ',encoding='GB2312')
        #保存为csv格式
        #all1.to_csv('all.csv',encoding='GB2312')'''
def concattxt():
    with open('f:/btcdata/all.txt','r',encoding='gb2312')as f:
        data=f.readlines()
    f.close()
    #df = DataFrame(data, index=['time'], columns=['open', 'close', 'high', 'low', 'volume'])
    header=['time','open','close','high','low','volume']
    with open('f:/btcdata/merge.csv', 'wb',encoding='utf-8') as dstfile:  # 写入方式选择wb，否则有空行
        writer = csv.DictWriter(dstfile, fieldnames=header)
        writer.writeheader()  # 写入表头
        writer.writerows(data)  # 批量写入
    dstfile.close()



if __name__ == '__main__':
    #txtcombine()
    concattxt()
