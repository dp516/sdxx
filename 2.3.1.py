'''
@Descripttion: 简单感知机 
@version: 
@Author: stephendp
@Date: 2019-10-20 00:36:33
@LastEditors: stephendp
@LastEditTime: 2019-10-20 00:39:33
'''
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print(AND(0, 0))

