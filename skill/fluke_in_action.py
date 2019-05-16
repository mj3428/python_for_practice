#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import datetime
import numpy as np
import arrow

df = pd.read_excel('1#fluke.xlsx', index_col=None)
df['时间'] = df['时间'].apply(lambda x: str(x).split('.')[0])
df['日期'] = df['日期'].apply(lambda x: datetime.datetime.strftime(x, '%Y-%m-%d'))
df.insert(0, 'datetime', df['日期'].map(str) + ' ' + df['时间'])
# df['datetime'] = df['日期'].map(str) + ' ' +df['时间']
df.drop(['日期', '时间'], axis=1, inplace=True)
df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d %H:%M:%S')
df = df.groupby([pd.Grouper(key='datetime', freq='60s')]).mean()#聚合
#print(df.columns.values.tolist())
#print(df.head(12))
df.to_excel('1#data_fluke.xlsx', sheet_name='fluke')
