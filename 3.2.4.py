'''
@Descripttion: sigmoid函数可视化
@version: 
@Author: stephendp
@Date: 2019-10-20 18:03:35
@LastEditors: stephendp
@LastEditTime: 2019-10-20 18:09:00
'''
import numpy as np
import matplotlib.pylab as plt

"""
sigmoid函数
"""
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()
