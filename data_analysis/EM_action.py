
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('March.xlsx', index_col='用户', encoding = 'gb18030')
print(df.head(5))
features = [u'高危功率因数', u'高危电压谐波', u'高危负荷率', u'高危谐波电流', u'高危变压器电流', u'隐患功率因数',
            u'隐患电流不平衡', u'隐患电压谐波', u'隐患负荷率',u'隐患设备故障', u'隐患谐波电流', u'隐患变压器电流', u'隐患电压',
            u'日志变压器电流', u'日志负荷率']
data = df[features]

# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

corr = data[features].corr()
plt.figure(figsize=(11, 9))
# annot=True 显示每个方格的数据
sns.heatmap(corr, annot=True)
#plt.savefig('./pic/corr.png')
plt.show()

features_remain = [u'高危功率因数', u'隐患功率因数',u'高危电压谐波', u'隐患电压谐波', u'隐患设备故障', u'隐患电流不平衡',
                   u'隐患电压', u'日志变压器电流', u'日志负荷率']
data = df[features_remain]
# 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
ss = StandardScaler()
data = ss.fit_transform(data)
# 构造 GMM 聚类 n_component为聚类个数
gmm = GaussianMixture(n_components=12, covariance_type='full')
gmm.fit(data)
# 训练数据
prediction = gmm.predict(data)
print(prediction)
# 将分组结果输出到 CSV 文件中
df.insert(0, '分组', prediction)
df.to_csv('pre_out.csv', index=False, sep=',')

from sklearn.metrics import calinski_harabaz_score
print(calinski_harabaz_score(data, prediction))
