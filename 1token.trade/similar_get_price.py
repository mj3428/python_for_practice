##从onepy取一个cleaner打算用于提取ticker，来替代聚宽的get_price模块
from collections import defaultdict, deque
from functools import partial
from itertools import count

import arrow

from OnePy.sys_module.metabase_env import OnePyEnvBase


class CleanerBase(OnePyEnvBase):
    cleaner_counter = count(1)

    def __init__(self, rolling_window, buffer_day):
        self.name = f'{self.__class__.__name__}_{next(self.cleaner_counter)}'
        self.env.cleaners.update({self.name: self})
        self.rolling_window = rolling_window
        self.buffer_day = buffer_day
        self.retry = count(1)
        self.data = None

    @property
    def startdate(self):
        date = arrow.get(self.env.fromdate).shift(days=-self.buffer_day)

        return date.format('YYYY-MM-DD HH:mm:ss')

    def _check_length(self, ticker):
        if len(self.data[ticker]) < self.data[ticker].maxlen:

            self.buffer_day += 2
            self.initialize_buffer_data()

            self.env.logger.warning(
                f'{self.name} buffer_day is too short! Retry No.{next(self.retry)} times')

    def initialize_buffer_data(self):
        self.data = defaultdict(partial(deque, maxlen=self.rolling_window))

        for key, value in self.env.readers.items():
            buffer_data = value.load(
                fromdate=self.startdate, todate=self.env.fromdate)

            self.data[key].extend((i['close'] for i in buffer_data))
            self._check_length(key)

    def _append_data_to_buffer(self):
        for ticker, ohlc in self.env.feeds.items():
            self.data[ticker].append(ohlc.close)

    def run(self):
        self._append_data_to_buffer()

    def calculate(self, ticker):
        raise NotImplementedError
###
#按照po主给的思路
#
#key为ticker
#取readers
#给load函数提供from date函数和todate函数就可以
#想多少就取多少
#按日期取
#写cleaner
#以下是mongodb load里的load 区别于 csvreader的load
def load(self, fromdate=None, todate=None):
    coll = self.set_collection()
    if fromdate is None:
        fromdate = self.fromdate

    if todate is None:
        todate = self.todate

    if fromdate and todate:
        return coll.find({'date': {'$gte': fromdate, '$lt': todate}})
    elif fromdate:
        return coll.find({'date': {'$gte': fromdate}})
    elif todate:
        return coll.find({'date': {'$lt': todate}})
    else:
        return coll.find()
