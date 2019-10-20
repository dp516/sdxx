'''
@Descripttion: RELU函数可视化
@version: 
@Author: stephendp
@Date: 2019-10-20 18:10:46
@LastEditors: stephendp
@LastEditTime: 2019-10-20 18:15:13
'''
import numpy as np
import matplotlib.pylab as plt

"""
RELU函数
"""
def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5) # 指定y轴的范围
plt.show()
