'''
@Descripttion: 构造异或门 
@version: 
@Author: stephendp
@Date: 2019-10-20 11:19:17
@LastEditors: stephendp
@LastEditTime: 2019-10-20 17:39:41
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

"""
异或门
"""
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))