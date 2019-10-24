'''
@Descripttion: 输出层 softmax函数
@version: 
@Author: stephendp
@Date: 2019-10-24 21:50:41
@LastEditors: stephendp
@LastEditTime: 2019-10-24 22:00:01
'''
import numpy  as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y