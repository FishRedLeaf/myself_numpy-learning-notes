# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:22:15 2018

@author: Administrator
使用数组创建例程
Routine例程
"""

import numpy as np

'''
numpy.empty(shape, dtype = float, order = 'C')
1.	Shape 空数组的形状，整数或整数元组
2.	Dtype 所需的输出数组类型，可选
3.	Order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
numpy.zeros(shape, dtype = float, order = 'C')
numpy.ones(shape, dtype = None, order = 'C')

'''
#数组元素为随机值，因为它们未初始化
x1 = np.empty([3,2], dtype =  int) 
print(x1)
#含有 5 个 0 的数组，默认类型为 float
x2 = np.zeros([3,2], dtype =  int) 
print(x2)
x22 = np.zeros((5,), dtype = np.int)
print(x22)
x222 = np.zeros((2,2), dtype =  [('x',  'i4'),  ('y',  'f4')])
print(x222); print(x222['x']); print(x222['y'])
#含有 5 个 1 的数组，默认类型为 float
x3 = np.ones(5); print(x3)
x33 = np.ones([2,2], dtype =  int);print(x33)  