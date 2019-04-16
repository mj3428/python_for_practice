# -*- coding: utf-8 -*-
# 信用卡违约率分析
import pandas as pd
from sklearn.model_selection import learning_curve, train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier

from matplotlib import pyplot as plt
import seaborn as sns
# 数据加载
data = pd.read_csv('./UCI_Credit_Card.csv')
# 数据探索
print(data.shape) # 查看数据集大小
print(data.describe()) # 数据集概览
# 查看下一个月违约率的情况
next_month = data['default.payment.next.month'].value_counts()
print(next_month)
df = pd.DataFrame({'default.payment.next.month': next_month.index,'values': next_month.values})
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.figure(figsize = (6,6))
plt.title('信用卡违约率客户\n (违约：1，守约：0)')
sns.set_color_codes("pastel")
sns.barplot(x = 'default.payment.next.month', y="values", data=df)
locs, labels = plt.xticks()
plt.show()
# 特征选择，去掉ID字段、最后一个结果字段即可
data.drop(['ID'], inplace=True, axis =1) #ID这个字段没有用
target = data['default.payment.next.month'].values
columns = data.columns.tolist()
columns.remove('default.payment.next.month')
features = data[columns].values
# 30%作为测试集，其余作为训练集
train_x, test_x, train_y, test_y = train_test_split(features, target, test_size=0.30, stratify = target, random_state = 1)


#分类器
ada=AdaBoostClassifier( random_state=1)
#需要调整的参数
parameters={'n_estimators':[10,50,100]}

# 使用 GridSearchCV 进行参数调优
clf=GridSearchCV(estimator=ada,param_grid=parameters,scoring = 'accuracy')

clf.fit(train_x,train_y)
print("GridSearch最优参数：", clf.best_params_)
print("GridSearch最优分数： %0.4lf" %clf.best_score_)
predict_y=clf.predict(test_x)
print("准确率 %0.4lf" %accuracy_score(test_y, predict_y))


'''
1.对GridSearchCV的理解：就是在之前的经验的基础上选择了一些较好的取值备选，
然后分别去试，得到一个好的性能。比直接选择参数多了一些保障，但是也增加一些计算负担。

Name: default.payment.next.month, dtype: int64
GridSearch最优参数： {'n_estimators': 10}
GridSearch最优分数： 0.8187
准确率 0.8129
'''
