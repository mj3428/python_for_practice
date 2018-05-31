# -python
用python来做数字货币
#python版 Dual Thrust OKCoin 期货  (Copy)
现在拓展思维，不单单是道氏理论，更多来用于整体的学习

声明：

#
#Python 3最重要的新特性大概要算是对文本和二进制数据作了更为清晰的区分。文本总是Unicode，由str类型表示，二进制数据则由bytes类型表示。
Python 3不会以任意隐式的方式混用str和bytes，正是这使得两者的区分特别清晰。
你不能拼接字符串和字节包，也无法在字节包里搜索字符串（反之亦然），也不能将字符串传入参数为字节包的函数（反之亦然）.
#

#运行顺序：
--># get_candles # 下载K线数据
--># merge.py # 合并用到createVar
--># change_utc8.py #处理数据类型
--># change_colname.py #改变列名称
