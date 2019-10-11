# Task

## 算法：

+ **目的：使研究生们尽快熟悉人工智能、机器学习与大数据领域的基础算法。**

+ **要求：**

1. 理解算法本身，用程序设计语言（不限语言，但建议选择Python、C、C++、或Java）实现算法。

2. **除了数学运算（例如求函数值、矩阵求逆等）可以调用现有的库函数，其他一律不准调库。**

3. **报告内容按模板撰写，并提交源程序文件**

+ 内容：实现以下4个算法

1. **Kmeans**：在二维平面上随机生成20个点，利用Kmeans方法将点聚成3类，聚类结果需用**Echarts**进行可视化。
2. **Logistic Regression**：利用附件提供的**Abalone**数据http://archive.ics.uci.edu/ml/datasets/Abalone，**80%**用于训练，**20%**用于测试，给出实验的F score。提醒：由于是LR用于二分类，所以需要剔除掉数据中第一项为I的那些数据。
3. **Softmax Regreesion：**利用上述同样的数据，完成三分类，给出分类的准确率。
4. **BP神经网络：**实现异或分类，即（0,0）和（1,1）为0；（1,0）和（0,1）为1



---



# K-means

1. generate_random_dots

   ```python
   import random
   from matplotlib.pyplot import *
   
   all_points=[]
   for i in range(20):
       generate_date=[random.randint(1,100),random.randint(1,100)]
       if not generate_date in all_points:
           all_points.append(generate_date)
   
   for i in range(20):
       plot(all_points[i][0],all_points[i][1],"x")
   
   show()
   ```

2. using K-means to classify

```python

```
(1).随机选取中心点
(2).重复计算欧式距离
(3).得到确定质心位置
(4).以当前获得的质心，进行距离计算，归类



## # sklearn.cluster.Kmeans 参数介绍

-------------

**参数**：
n_clusters：整型，缺省值=8 【生成的聚类数，即产生的质心（centroids）数。】
max_iter：整型，缺省值=300,执行一次k-means算法所进行的最大迭代数。
n_init：整型，缺省值=10
用不同的质心初始化值运行算法的次数，最终解是在inertia意义下选出的最优结果。
init：有三个可选值：’k-means++’， ‘random’，或者传递一个ndarray向量。
此参数指定初始化方法，默认值为 ‘k-means++’。
（１）‘k-means++’ 用一种特殊的方法选定初始质心从而能加速迭代过程的收敛（即上文中的k-means++介绍）
（２）‘random’ 随机从训练数据中选取初始质心。
（３）如果传递的是一个ndarray，则应该形如 (n_clusters, n_features) 并给出初始质心。
precompute_distances：三个可选值，‘auto’，True 或者 False。
预计算距离，计算速度更快但占用更多内存。
（１）‘auto’：如果 样本数乘以聚类数大于 12million 的话则不预计算距离。This corresponds to about 100MB overhead per job using double precision.
（２）True：总是预先计算距离。
（３）False：永远不预先计算距离。
tol：float形，默认值= 1e-4　与inertia结合来确定收敛条件。
n_jobs：整型数。　指定计算所用的进程数。内部原理是同时进行n_init指定次数的计算。
（１）若值为 -1，则用所有的CPU进行运算。若值为1，则不进行并行运算，这样的话方便调试。
（２）若值小于-1，则用到的CPU数为(n_cpus + 1 + n_jobs)。因此如果 n_jobs值为-2，则用到的CPU数为总CPU数减1。
random_state：整形或 numpy.RandomState 类型，可选
用于初始化质心的生成器（generator）。如果值为一个整数，则确定一个seed。此参数默认值为numpy的随机数生成器。
copy_x：布尔型，默认值=True
当我们precomputing distances时，将数据中心化会得到更准确的结果。如果把此参数值设为True，则原始数据不会被改变。如果是False，则会直接在原始数据
上做修改并在函数返回值时将其还原。但是在计算过程中由于有对数据均值的加减运算，所以数据返回后，原始数据和计算前可能会有细小差别。

**(轮廓系数)**在实际应用中，由于Kmean一般作为数据预处理，或者用于辅助分聚类贴标签。所以k一般不会设置很大。可以通过枚举，令k从2到一个固定值如10，在每个k值上重复运行数次kmeans(避免局部最优解)，并计算当前k的平均轮廓系数，最后选取轮廓系数最大的值对应的k作为最终的集群数目。







