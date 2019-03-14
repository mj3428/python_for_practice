# -*- coding: utf-8 -*-
from pandas import DataFrame, Series
import pandas as pd; import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY,YEARLY
from matplotlib.dates import MonthLocator,MONTHLY
import datetime as dt


import pylab

daylinefilespath = 'e:\\'
stock_b_code = '200000' 
MA1 = 10
MA2 = 20
MA3 = 5
startdate = dt.date(2017, 3, 1)
enddate = dt.date(2017, 9, 19)


def readstkData(rootpath, stockcode, sday, eday):
    
    returndata = pd.DataFrame()
    for yearnum in range(0,int((eday - sday).days / 365.25)+1):
        theyear = sday + dt.timedelta(days = yearnum * 365)
        # build file name
        filename = rootpath  + theyear.strftime('%Y') + '\\' + str(stockcode).zfill(6) + '.csv'
        print(filename)
        
        try:
            rawdata = pd.read_csv(filename, parse_dates = True, index_col = 0, encoding = 'gbk')
        except IOError:
           raise Exception('IoError when reading dayline data file: ' + filename)

        returndata = pd.concat([rawdata, returndata])
    
    # Wash data
    returndata = returndata.sort_index()
    returndata.index.name = 'DateTime'
    #returndata.drop('price_change', axis=1, inplace = True)

    returndata.columns = ['Open', 'High', 'Close', 'Low', 'Volume']

    returndata = returndata[returndata.index < eday.strftime('%Y-%m-%d')]
    print(enddate)
    return returndata
def main():
    days = readstkData(daylinefilespath, stock_b_code, startdate, enddate)

    # drop the date index from the dateframe & make a copy
    daysreshape = days.reset_index()
    # convert the datetime64 column in the dataframe to 'float days'
    daysreshape['DateTime']=mdates.date2num(daysreshape['DateTime'].astype(dt.date))
    # clean day data for candle view 
    daysreshape.drop('Volume', axis=1, inplace = True)
    daysreshape = daysreshape.reindex(columns=['DateTime','Open','High','Low','Close'])  
    
    MA10 = pd.rolling_mean(daysreshape.Close.values, MA1)
    MA20 = pd.rolling_mean(daysreshape.Close.values, MA2)
    SP = len(daysreshape.DateTime.values[MA2-1:])
    countmkt = len(daysreshape.DateTime.values[0:])
    fig = plt.figure(facecolor='#07000d',figsize=(15,10))
    
    ax1 = plt.subplot2grid((6,4), (1,0), rowspan=4, colspan=4, axisbg='#07000d')
    candlestick_ohlc(ax1, daysreshape.values[-countmkt:], width=.6, colorup='#ff1717', colordown='#53c156')
    Label1 = str(MA1)+' SMA'
    Label2 = str(MA2)+' SMA'

    AA_input = (daysreshape.Close.values*2+daysreshape.High.values+daysreshape.Low.values)/4  #(2*CLOSE+HIGH+LOW)/4
    AA = pd.rolling_mean(AA_input, MA3) #AA:=MA((2*CLOSE+HIGH+LOW)/4,5);
    XS_1 = [AA[i]*102/100 for i in range(SP)]  #ͨ��1:AA*N/100;
    XS_2 = [AA[i]*(200-102)/100 for i in range(SP)]	#ͨ��2:AA*(200-N)/100;
    CC_input = AA_input   #(2*CLOSE+HIGH+LOW)/4
    ABS_input=[CC_input[i]-MA20[i] for i in range(SP)]   #((2*CLOSE+HIGH+LOW)/4-MA(CLOSE,20))
    ABS = [abs(ABS_input[i]) for i in range(SP)]	
    #CC:=ABS((2*CLOSE+HIGH+LOW)/4-MA(CLOSE,20))/MA(CLOSE,20); 
    CC = [ABS[i]/MA20[i] for i in range(SP)] 
    print (SP)
    print (CC)
    
    ax1.plot(daysreshape.DateTime.values[-SP:],MA10[-SP:],'#e1edf9',label=Label1, linewidth=1.5)
    ax1.plot(daysreshape.DateTime.values[-SP:],MA20[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
    #ax1.plot(daysreshape.DateTime.values[-SP:],XS_1[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
    #ax1.plot(daysreshape.DateTime.values[-SP:],XS_2[-SP:],'#e1edf9',label=Label2, linewidth=1.5)
    ax1.grid(True, color='w')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.label.set_color("w")
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.tick_params(axis='y', colors='w')
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
    ax1.tick_params(axis='x', colors='w')
    plt.ylabel('Stock price and Volume')
    plt.show()

if __name__ == "__main__":
    main()
