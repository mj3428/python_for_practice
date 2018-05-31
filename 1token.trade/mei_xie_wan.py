%matplotlib inline
import statsmodels.api as sm
from pandas.stats.api import ols
from pandas import DataFrame
import OnePy as op
from OnePy.builtin_module.recorders.stock_recorder import StockRecorder
from OnePy.custom_module.cleaner_sma import SMA
global N,M,init,buy,sell,ans,ans_rightdev
init=True
N=18
M=300
buy=7
sell=7
ans=[]
ans_right=[]
class SmaStrategy(op.StrategyBase):

    def __init__(self):
        super().__init__()
    def initial():
        global N,M,ans,ans_rightdev
        N=18
        M=300
        prices=op.data_readers.CSVReader('e:/binancedata/merge2.csv', 'merge2',fromdate='2017-08-17 20:00:00', todate='2018-05-12 14:00:00')
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

def main():
    global init
    SS=SmaStrategy()
    beta=0
    r2=0
    if init:
        init=False
    else:
        prices=
    
    
    



#op.data_readers.CSVReader('e:/binancedata/merge2.csv', 'merge2',fromdate='2017-08-19', todate='2018-01-01')


#SmaStrategy()

op.RiskManagerBase()
op.StockBroker()

StockRecorder().set_setting(initial_cash=5000000,comm=0.998, comm_pct=None, margin_rate=1)

go = op.OnePiece()
# go.show_log(file=False)
go.sunny()
# go.output.show_setting()
go.output.plot('merge2')
print(go.output.trade_log())
