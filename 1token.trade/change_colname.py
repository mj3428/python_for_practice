#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import datetime
from pandas import DataFrame
if __name__ == '__main__':
    df=pd.read_csv('e:/binancedata/merge1.csv')
    #print(df.columns)
    df.rename(columns={'time':'date'}, inplace=True)
    df.to_csv('e:/binancedata/merge2.csv')
