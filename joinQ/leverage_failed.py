import numpy as np
import statsmodels.api as sm
from pandas.stats.api import ols
from pandas import DataFrame
from datetime import datetime
import talib
import pandas as pd
import scipy as sp
import scipy.optimize
from jqdata import gta
import jqdata
# 初始化函数，设定基准等等
def initialize(context):
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    
    run_daily(market_open,time='every_bar')
    
    run_daily(after_market_close, time='after_close', reference_security='000300.XSHG')

def shift_trading_day(date_,shift_):
    # 获取所有的交易日，返回一个包含所有交易日的 list,元素值为 datetime.date 类型.
    tradingday = jqdata.get_trade_days(start_date='2018-01-01')
    # 得到date之后shift天那一天在列表中的行标号 返回一个数
    shiftday_index = list(tradingday).index(date_) + shift_
    # 根据行号返回该日日期 为datetime.date类型
    return tradingday[shiftday_index]

def to_date(date_string_):
    return datetime.strptime(date_string_, '%Y-%m-%d').date()
def to_date_string(date_):
    return date_.strftime('%Y-%m-%d')

def market_open(context):
    current_data = get_current_data()
    statsDate=context.current_dt.strftime("%Y-%m-%d")
    buy_list=[]
    buy_list=fun_get_stock_list(context,None)
    log.info(buy_list)
    value0 = context.portfolio.cash/10
    for stock in buy_list:
        if len(buy_list) >= 3 and len(buy_list) <= 10 and context.portfolio.available_cash > 20000:
            order_value(stock,value0)

        if len(buy_list) > 10 and context.portfolio.available_cash > 20000:
            value1 = context.portfolio.cash/len(buy_list)
            order_value(stock,value1)
    
    if context.portfolio.positions.keys() !=[]:
        for stock in context.portfolio.positions.keys():
            last_buy_time =context.portfolio.positions[stock].transact_time
            d1 =last_buy_time.strftime('%Y-%m-%d')
            d2 = datetime.strptime(d1, '%Y-%m-%d')
            hold_days = jqdata.get_trade_days(start_date=d2, end_date=statsDate).size
            hd = abs(hold_days)
            value = context.portfolio.positions[stock].value
            if hd >= 1:
                hprice = attribute_history(stock, hd, '1d', 'high', df=False)
                sec_hprice = hprice['high'].tolist()
                hhprice = max(sec_hprice)
                #log.info(hhprice)
                h_return = (hhprice - context.portfolio.positions[stock].avg_cost)/context.portfolio.positions[stock].avg_cost*100.0
                #log.info(h_return,hhprice,context.portfolio.positions[stock].avg_cost)
                cur_price = current_data[stock].last_price
                #log.info(cur_price)
                win = (cur_price - context.portfolio.positions[stock].avg_cost)/context.portfolio.positions[stock].avg_cost* 100.0
                position = context.portfolio.positions[stock]
                retrace = h_return-win
                #log.info("retrace is %s"%retrace)

                if h_return<10.0 and retrace >= 3.8 and stock not in buy_list:
                    order_target_value(stock,0)
                    log.info("Sell %s for gegu stoploss 3.8dian" %stock,h_return,hhprice,retrace)
        
                if len(buy_list) < 3 and stock not in buy_list:
                    order(stock,-0.5*value)
            if hd==5:
                order_target_value(stock,0)
    
    
def fun_get_stock_list(context,statsDate=None):
    g.quantlib  = quantlib()
    buyout=[]
    buyout=get_marginsec_stocks()
    
    df = get_fundamentals(
        query(valuation.code,valuation.market_cap, valuation.pe_ratio,  
        valuation.pb_ratio))

        # 1) 总市值全市场从大到小前80%
    fCap = df.sort(['market_cap'], ascending=[False])
    fCap = fCap.reset_index(drop = True)
    fCap = fCap[0:int(len(fCap)*0.9)]
    sListCap = list(fCap['code'])

        # 2）市盈率全市场从小到大前40%（剔除市盈率为负的股票）
    fPE = df.sort(['pe_ratio'], ascending=[True])
    fPE = fPE.reset_index(drop = True)
    fPE = fPE[fPE.pe_ratio > 0]
    fPE = fPE.reset_index(drop = True)
    fPE = fPE[0:int(len(fPE)*0.7)]
    sListPE = list(fPE['code'])

    # 3）pb全市场从小到大前40%（剔除pb为负的股票）
    fPB = df.sort(['pb_ratio'], ascending=[True])
    fPB = fPB.reset_index(drop = True)
    fPB = fPB[fPB.pb_ratio > 0]
    fPB = fPB.reset_index(drop = True)
    fPB = fPB[0:int(len(fPB)*0.7)]
    sListPB = list(fPB['code'])

    # 5）同时满足上述3条的股票，按照股息率从大到小排序，选出股息率最高的 n 只股票
    good_stocks = list(set(sListCap) & set(sListPE) & set(sListPB)&set(buyout))
    yinhang = get_industry_stocks('J66')
    good_stocks = list(set(good_stocks).difference(set(yinhang)))
    log.info(len(good_stocks))
    #print len(good_stocks)
    
    Today = context.current_dt.strftime("%Y-%m-%d")
    LAday = shift_trading_day(to_date(Today),-1)

    wanna=[]
    out_stocks=[]
    #df = jqdata.get_mtss(good_stocks,Lastday,Today,fields=["date","sec_code","fin_value","fin_buy_value"])
    for stock in good_stocks:
        
        h=history(1, '1d', 'close',stock, df=False)
        currentP=h[stock][0]
        prices = attribute_history(stock,300,'1d','close',df=False)
        #MA10= prices['close'][-10:].mean()
        #MA5 = prices['close'][-5:].mean()
        MA60 = prices['close'][-60:].mean()
        MA30 = prices['close'][-30:].mean()
        bb  = attribute_history(stock,750,'1d',['high','low'],df=False)
        bhh = max(bb['high'].tolist())
        bll = min(bb['low'].tolist())
        sl  = attribute_history(stock,60,'1d','low',df=False)
        sll = min(sl['low'].tolist())
        
        three =attribute_history(stock,3,'1d','low',df=False)
        fif = attribute_history(stock,15,'1d','low',df=False)
        three_low = min(three['low'].tolist())
        fif_low = min(three['low'].tolist())
        
        if sll <= (1.08*bll) or (sll/bhh) > 0.4 or sll > (1.58*bll) or three_low < fif_low or MA30 < MA60:
            out_stocks.append(stock)
        
        df = jqdata.get_mtss(stock,end_date=LAday,fields=["date","sec_code","fin_value"],count=3)
        #log.info(df)
        #data=df.set_index('sec_code')
        aa=np.array([df['sec_code'],df['fin_value']])
        #log.info(aa)
        if aa!=[] and len(aa[0])==3:
            if aa[1,0] >= aa[1,1] or aa[1,1] >= aa[1,2]:
                out_stocks.append(aa[0,0])
        #log.info(out_stocks)
    wanna=list(set(good_stocks).difference(set(out_stocks)))
    
    
    detail=jqdata.get_mtss(wanna,end_date=LAday,fields=["date", "sec_code", "fin_value", "fin_buy_value"],count=1)
    detail.rename(columns={'sec_code':'code'}, inplace=True) 
    
    df = get_fundamentals(query(valuation.code,valuation.market_cap),date = LAday )
    df = df[df.code.isin(wanna)]
    df = df.reset_index(drop = True)
    #log.info(df)
    merge = pd.merge(detail,df,on='code')
    merge['buy_proportion']= 100.0*(merge['fin_buy_value']/merge['fin_value'])
    merge['liquidity'] = 100.0*(merge['fin_value']/(merge['market_cap']*100000000.0))
    merge['score'] = (0.4/abs(merge['liquidity']-0.401))*70.0+(12/abs(merge['buy_proportion']-12.001))*30.0
    
    merge = merge[merge.score > 39.9]
    merge = merge.reset_index(drop=True)
    merge = merge.sort(columns='score',ascending=False)
    merge = merge.reset_index(drop=True)
    sMerge=list(merge['code'])
    #log.info(len(sMerge))
    #log.info(sMerge)
    positions_list = context.portfolio.positions.keys()
    sMerge = g.quantlib.unpaused(sMerge, positions_list)
    sMerge = g.quantlib.remove_st(sMerge, Today)
    sMerge = g.quantlib.remove_limit_up(sMerge, positions_list)
    log.info(len(sMerge))
    #log.info(sMerge)
    return sMerge
    
    
class quantlib():

    #下面的都是细节处理
    def unpaused(self, stock_list, positions_list):
        current_data = get_current_data()
        tmpList = []
        for stock in stock_list:
            if not current_data[stock].paused or stock in positions_list:
                tmpList.append(stock)
        return tmpList

    def remove_st(self, stock_list, statsDate):
        current_data = get_current_data()
        return [s for s in stock_list if not current_data[s].is_st]

    # 剔除涨停板的股票（如果没有持有的话）
    def remove_limit_up(self, stock_list, positions_list):
        h = history(1, '1m', 'close', stock_list, df=False, skip_paused=False, fq='pre')
        h2 = history(1, '1m', 'high_limit', stock_list, df=False, skip_paused=False, fq='pre')
        tmpList = []
        for stock in stock_list:
            if h[stock][0] < h2[stock][0] or stock in positions_list:
                tmpList.append(stock)
        return tmpList

def after_market_close(context):
    trades = get_trades()
    for _trade in trades.values():
        log.info('成交记录：'+str(_trade))
