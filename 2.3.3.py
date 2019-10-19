'''
@Descripttion: 简单感知机：与门、与非门和或门
@version: 
@Author: stephendp
@Date: 2019-10-20 01:13:35
@LastEditors: stephendp
@LastEditTime: 2019-10-20 01:30:25
'''
import numpy as np

"""
与门
"""
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # 权重
    b = -0.7 # 偏置。决定了神经元被激活的容易程度
    
    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

"""
与非门
"""
def NAND(x1, x2):
    x = np.array([x1, x2])
    # 权重和偏置不同
    w = np.array([-0.5, -0.5]) # 权重
    b = 0.7 # 偏置。决定了神经元被激活的容易程度
    
    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

"""
或门
"""
def OR(x1, x2):
    x = np.array([x1, x2])
    # 权重和偏置不同
    w = np.array([0.5, 0.5]) # 权重
    b = -0.2 # 偏置。决定了神经元被激活的容易程度
    
    tmp = np.sum(w*x) + b

    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(1, 1))
print(NAND(1, 1))
print(OR(1, 1))
