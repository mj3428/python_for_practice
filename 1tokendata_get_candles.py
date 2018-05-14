###第一步####下载数据
#因为之前是下载的txt数据，这里下载的数据将改为.json格式，且每次取15min数据只能取2天，因此循环的时候2天为一个json文件
import datetime
import urllib.request

if __name__=="__main__":
    startdate=datetime.date(2017,8,17)
    enddate=datetime.date(2018,5,11)
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
##################
####第二步######将所有的json的数据提取出来合并成一张csv报表，难度是解析json的字典文件（庆幸的是只有一级字典）
import pandas
import codecs
import glob
import pandas as pd
from pandas import DataFrame
import datetime
import json
import collections

def concattxt():
    startdate = datetime.date(2017, 8, 17)
    enddate = datetime.date(2018, 5, 11)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    n=0
    list=[]
    for i in range((enddate - startdate).days + 1):
        if i % 2 == 0:
            day1 = startdate + datetime.timedelta(days=i)
            day2 = startdate + datetime.timedelta(days=i + 2)
            # print(type(data))
            load_f=open("e:/binancedata/" + str(day1) + "-" + str(day2) + ".json",)
            load_dict=json.load(load_f)
            #print(load_dict)
            dd1=[flatten(j) for j in load_dict]
            createVar['d' + str(n)] = pd.DataFrame(dd1,columns=['time','close','high','low','open','volume','contract'])
            list.append(createVar['d' + str(n)])
            n=n+1
    MG=pd.concat(list)
    MG.to_csv("e:/binancedata/merge.csv",index=None)

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

if __name__ == '__main__':
    createVar = locals()
    concattxt()
###总结 总共两个py文件 第一个用于下载数据，第二个合并数据，新知识createVar中的locals是python的内置函数，可以用于建立动态的自变量
