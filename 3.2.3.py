'''
@Descripttion: 阶跃函数可视化 
@version: 
@Author: stephendp
@Date: 2019-10-20 17:55:19
@LastEditors: stephendp
@LastEditTime: 2019-10-20 18:01:31
'''
import numpy as np
import matplotlib.pylab as plt

"""
阶跃函数
"""
def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # 指定y轴的范围
plt.show()
