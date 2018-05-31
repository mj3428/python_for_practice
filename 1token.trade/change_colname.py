#!/usr/bin/env python
# encoding: utf-8
'''
@author: caopeng
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: change_colname.py
@time: 2018-05-21 13:11
@desc:
'''

import pandas as pd
import datetime
from pandas import DataFrame
if __name__ == '__main__':
    df=pd.read_csv('e:/binancedata/merge1.csv')
    #print(df.columns)
    df.rename(columns={'time':'date'}, inplace=True)
    df.to_csv('e:/binancedata/merge2.csv')