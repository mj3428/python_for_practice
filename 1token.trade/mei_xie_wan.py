%matplotlib inline
import numpy as np
import statsmodels.api as sm
import pandas.stats.api as ols
from pandas import DataFrame
import OnePy as op
from OnePy.builtin_module.recorders.stock_recorder import StockRecorder
from OnePy.sys_module.base_cleaner import CleanerBase
global N,M,init,buy,sell,ans,ans_rightdev
init=True
N=18
M=300
buy=7
sell=7
ans=[]
ans_right=[]
class attribute(CleanerBase):
    def calculatehighs(self,ticker):
        self.data = defaultdict(partial(deque, maxlen=self.rolling_window))
        for key, value in self.env.readers.items():
            buffer_data = value.load(
                fromdate=self.startdate, todate=self.env.fromdate)

            self.data[key].extend((i['high'] for i in buffer_data))
            self._check_length(key)
        highs=self.dara[ticker]
        
    def calculatelows(self,ticker):
        self.data = defaultdict(partial(deque, maxlen=self.rolling_window))
        for key, value in self.env.readers.items():
            buffer_data = value.load(
                fromdate=self.startdate, todate=self.env.fromdate)

            self.data[key].extend((i['low'] for i in buffer_data))
            self._check_length(key)
        lows=self.dara[ticker]
    
class SmaStrategy(op.StrategyBase):

    def __init__(self):
        super().__init__()
    def initial(slef):
        global N,M,ans,ans_rightdev
        
        N=18
        M=300
        
        main(self)
        
        prices=op.data_readers.CSVReader('e:/binancedata/merge2.csv', 'merge2',fromdate='2017-08-18 08:00:00', todate='2018-05-12 14:00:00')
        highs=prices.high
        lows=prices.low
        ans=[]
        for i in range(len(highs))[N:]:
            data_high = highs.iloc[i-N+1:i+1]
            data_low = lows.iloc[i-N+1:i+1]
            X = sm.add_constant(data_low)
            model = sm.OLS(data_high,X)
            results = model.fit()
            ans.append(results.params[1])
            #计算r2
            ans_rightdev.append(results.rsquared)
        
    '''def run_time():
        for h in range(0,24):
            for m in range(0,60,15):
                if m<=9:
                    m=('0'+str(m))
                    times.append(str(h)+':'+str(m))
        for item in times[:]:
            if item=='24:00':
                times.remove(item)
        return times'''

    def main(self):
        global init,ans_rightdev,ans,M,buy,sell
        
        beta=0
        r2=0
        if init:
            init=False
        else:
            a=attribute(50)
            highs=a.calculatehighs
            lows=a.calculatelows
            X = sm.add_constant(lows)
            model = sm.OLS(highs, X)
            beta = model.fit().params[1]
            ans.append(beta)
            #计算r2
            r2=model.fit().rsquared
            ans_rightdev.append(r2)
        section =ans[-M:]
        # 计算均值序列
        mu = np.mean(section)
        # 计算标准化RSRS指标序列
        sigma = np.std(section)
        zscore = (section[-1]-mu)/sigma
        #计算右偏RSRS标准分
        zscore_rightdev= zscore*beta*r2
    
        if zscore_rightdev > buy:
            self.buy(0.5, 'merge2', takeprofit=50,stoploss=10, trailingstop_pct=1)
        # 如果上一时间点的RSRS斜率小于卖出阈值, 则空仓卖出
        elif zscore_rightdev < sell:
            self.sell(0.5, 'merge2', takeprofit=50,stoploss=10, trailingstop_pct=1)
        

#op.data_readers.CSVReader('e:/binancedata/merge2.csv', 'merge2',fromdate='2017-08-19', todate='2018-01-01')

SmaStrategy()

op.RiskManagerBase()
op.StockBroker()

StockRecorder().set_setting(initial_cash=5000000,comm=0.998, comm_pct=None, margin_rate=1)

go = op.OnePiece()
# go.show_log(file=False)
go.sunny()
# go.output.show_setting()
go.output.plot('merge2')
print(go.output.trade_log())
