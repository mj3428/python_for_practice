##准备模拟数据
import numpy as np
from sklearn.datasets import make_regression
X, y = make_regression(1000, 2, noise=10)

#GBR算是一种集成模型因为它是一个集成学习算法,指GBR用许多较差的学习算法组成了一个更强大的学习算法
from sklearn.ensemble import GradientBoostingRegressor as GBR
gbr = GBR()
gbr.fit(X, y)
gbr_preds = gbr.predict(X)
#用基本回归算法来拟合数据当作参照：
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, y)
lr_preds = lr.predict(X)
#有了参照之后，让我们看看GBR算法与线性回归算法效果的对比情况
gbr_residuals = y - gbr_preds
lr_residuals = y - lr_preds

%matplotlib inline
from matplotlib import pyplot as plt

f, ax = plt.subplots(figsize=(7, 5))
f.tight_layout()
ax.hist(gbr_residuals,bins=20,label='GBR Residuals', color='b', alpha=.5);
ax.hist(lr_residuals,bins=20,label='LR Residuals', color='r', alpha=.5);
ax.set_title("GBR Residuals vs LR Residuals")
ax.legend(loc='best');
#看起来好像GBR拟合的更好，但是并不明显

#用95%置信区间（Confidence interval,CI）对比一下：
np.percentile(gbr_residuals, [2.5, 97.5])
array([-17.14322801,  17.05182403])
np.percentile(lr_residuals, [2.5, 97.5])
array([-19.79519628,  20.09744884])
#GBR的置信区间更小，数据更集中，因此其拟合效果更好

#优化方法：
n_estimators = np.arange(100, 1100, 350)
gbrs = [GBR(n_estimators=n_estimator) for n_estimator in n_estimators]
residuals = {}
for i, gbr in enumerate(gbrs):
    gbr.fit(X, y)
    residuals[gbr.n_estimators] = y - gbr.predict(X)

f, ax = plt.subplots(figsize=(7, 5))
f.tight_layout()
colors = {800:'r', 450:'g', 100:'b'}
for k, v in residuals.items():
    ax.hist(v,bins=20,label='n_estimators: %d' % k, color=colors[k], alpha=.5);
ax.set_title("Residuals at Various Numbers of Estimators")
ax.legend(loc='best');
#随着估计器数据的增加，误差在减少。
#不过，这并不是一成不变的。首先，我们没有交叉检验过，其次，随着估计器数量的增加，训练时间也会变长

##参数设置
'''
上面例子中GBR的第一个参数是n_estimators，指GBR使用的学习算法的数量。
通常，如果你的设备性能更好，可以把n_estimators设置的更大，效果也会更好。
还有另外几个参数要说明一下。

你应该在优化其他参数之前先调整max_depth参数。
因为每个学习算法都是一颗决策树，max_depth决定了树生成的节点数。
选择合适的节点数量可以更好的拟合数据，而更多的节点数可能造成拟合过度。

loss参数决定损失函数，也直接影响误差。l
s是默认值，表示最小二乘法（least squares）。
还有最小绝对值差值，Huber损失和分位数损失（quantiles）等等。
'''
