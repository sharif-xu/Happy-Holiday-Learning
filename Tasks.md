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

2.  using K-means to classify

