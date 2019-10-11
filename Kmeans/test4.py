from pyecharts import options as opts
from pyecharts.charts import Scatter
import numpy as np
from sklearn.cluster import KMeans
# 随机生成20个点
n=20
#每一个点的X值，正态分布
X=np.random.randint(0,100,n)
#每一个点的Y值
Y=np.random.randint(0,100,n)
Z=np.array(list(zip(X,Y))).reshape(len(X),2)
print(X)
print(Y)
print(Z)