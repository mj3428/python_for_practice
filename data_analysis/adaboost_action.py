import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score

# 设置 AdaBoost 迭代次数
n_estimators=200

# 数据加载
train_data=pd.read_csv('./Titanic_Data/train.csv')
test_data=pd.read_csv('./Titanic_Data/test.csv')

# 模块 2：数据清洗
# 使用平均年龄来填充年龄中的 NaN 值
train_data['Age'].fillna(train_data['Age'].mean(),inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(),inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)
# 使用登录最多的港口来填充登录港口Embarked的 nan 值
train_data['Embarked'].fillna('S',inplace=True)
test_data['Embarked'].fillna('S',inplace=True)

# 特征选择
features=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
train_features=train_data[features]
train_labels=train_data['Survived']
test_features=test_data[features]

# 将符号化的Embarked对象处理成0/1进行表示
dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
test_features=dvec.transform(test_features.to_dict(orient='record'))

# 决策树弱分类器
dt_stump = DecisionTreeClassifier(max_depth=1,min_samples_leaf=1)
dt_stump.fit(train_features, train_labels)

print(u'决策树弱分类器准确率为 %.4lf' % np.mean(cross_val_score(dt_stump, train_features, train_labels, cv=10)))

# 决策树分类器
dt = DecisionTreeClassifier()
dt.fit(train_features, train_labels)

print(u'决策树分类器准确率为 %.4lf' % np.mean(cross_val_score(dt, train_features, train_labels, cv=10)))

# AdaBoost 分类器
ada = AdaBoostClassifier(base_estimator=dt_stump,n_estimators=n_estimators)
ada.fit(train_features, train_labels)

print(u'AdaBoost 分类器准确率为 %.4lf' % np.mean(cross_val_score(ada, train_features, train_labels, cv=10)))
