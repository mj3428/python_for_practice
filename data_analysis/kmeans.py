# coding: utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
# 输入数据
data = pd.read_csv(r'./data.csv', encoding = 'gbk')
data.head()
train_x = data[["2019年国际排名","2018世界杯","2015亚洲杯"]]
df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=5)
# 规范化
min_max_scaler=preprocessing.StandardScaler()
train_x=min_max_scaler.fit_transform(train_x)
# kmeans 算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)


'''
两者的区别的比喻是，
Kmeans开班，选老大，风水轮流转，直到选出最佳中心老大
Knn小弟加队伍，离那个班相对近，就是那个班的

Kmeans
一群人的有些人想要聚在一起
首先大家民主（无监督学习）随机选K个老大（随机选择K个中心点）
谁跟谁近，就是那个队伍的人（计算距离，距离近的聚合到一块）
随着时间的推移，老大的位置在变化（根据算法，重新计算中心点）
直到选出真正的中心老大（重复，直到准确率最高）

Knn
一个人想要找到自己的队伍
首先听从神的旨意（有监督学习），随机最近的几个邻居
看看距离远不远（根据算法，计算距离）
近的就是一个班的了（属于哪个分类多，就是哪一类）
'''
