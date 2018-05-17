import pandas as pd
import datetime
from pandas import DataFrame
if __name__ == '__main__':
    df=pd.read_csv('e:/binancedata/merge.csv')
    df['time']=list(map(lambda y:y.split('+'),df['time']))
    df['time'] = list(map(lambda z:z.pop(0), df['time']))
    df['time'] = list(map(lambda a:a.replace(' ',''), df['time']))
    df['time']=list(map(lambda x:datetime.datetime.strptime(x,'%Y-%m-%dT%H:%M:%S')+datetime.timedelta(hours=8),df['time']))
    #print(df['time'])
    #print(type(df['time']))
    df['close']=list(map(lambda b:float(b),df['close']))
    df['high'] = list(map(lambda c: float(c), df['high']))
    df['low'] = list(map(lambda d: float(d), df['low']))
    df['open'] = list(map(lambda e: float(e), df['open']))
    df['volume']=list(map(lambda f:float(f),df['volume']))
    df.to_csv("e:/binancedata/merge1.csv",index=None)
