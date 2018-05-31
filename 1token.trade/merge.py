#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: merge.py
@time: 2018-05-14 9:01
@desc:
'''

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
    enddate = datetime.date(2018, 5, 28)
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
