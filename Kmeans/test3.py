from pyecharts import options as opts
from pyecharts.charts import Scatter
import numpy as np
from sklearn.cluster import KMeans
# 随机生成20个点
n=20
X=np.random.normal(0,1,n)#每一个点的X值，正态分布

Y=np.random.normal(0,1,n)#每一个点的Y值
Z=np.array(list(zip(X,Y))).reshape(len(X),2)
# 单独取出x矩阵，y矩阵
Zx, Zy=Z[:,0], Z[:,1]
# 运用KMeans方法进行聚类
km = KMeans(n_clusters=3).fit(Z)
# 聚类后的中心点集合
centroids=km.cluster_centers_
# 聚类后的标签
Zx_0, Zy_0, Zx_1, Zy_1, Zx_2, Zy_2=[], [], [], [], [], []
for x in range(0,20):
    km_label=km.labels_[x]
    if km_label == 0:
        Zx_0.append(Zx[x])
        Zy_0.append(Zy[x])
    elif km_label == 1:
        Zx_1.append(Zx[x])
        Zy_1.append(Zy[x])
    else:
        Zx_2.append(Zx[x])
        Zy_2.append(Zy[x])
# 矩阵化
Z_0 = np.array(list(zip(Zx_0,Zy_0))).reshape(len(Zx_0),2)
Z_1 = np.array(list(zip(Zx_1,Zy_1))).reshape(len(Zx_1),2)
Z_2 = np.array(list(zip(Zx_2,Zy_2))).reshape(len(Zx_2),2)
# 绘制散点图
def scatter_base() -> Scatter:
    c = (
        Scatter()
        # .add_xaxis(centroids[0:1,0])
        # .add_yaxis("Y_0", centroids[0:1,1], color='yellow', symbol='rect')
        .add_xaxis(Z_0[:,0])
        .add_yaxis("Y_0", Z_0[:,1], color='red')
        # .add_xaxis(centroids[1:2,0])
        # .add_yaxis("Y_0", centroids[1:2,1], color='yellow', symbol='rect')
        .add_xaxis(Z_1[:,0])
        .add_yaxis("Y_1", Z_1[:,1], color='yellow')
        # .add_xaxis(centroids[2:3,0])
        # .add_yaxis("Y_0", centroids[2:3,1], color='yellow', symbol='rect')
        .add_xaxis(Z_2[:,0])
        .add_yaxis("Y_2", Z_2[:,1], color='blue')
        .set_global_opts(
            title_opts=opts.TitleOpts(title="KMeans"),
            xaxis_opts=opts.AxisOpts(
                type_="value",
                min_=-3
                ),
            yaxis_opts=opts.AxisOpts(
                min_=-3
                )
            )
    )
    return c
# 函数调用
scatter_base().render()
