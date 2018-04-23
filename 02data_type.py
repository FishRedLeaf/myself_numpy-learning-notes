# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 10:27:49 2018

@author: Administrator

"""

import numpy as np

'''
ndarray对象
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
1.	object 任何暴露数组接口方法的对象都会返回一个数组或任何(嵌套)序列。
2.	dtype 数组的所需数据类型，可选。
3.	copy 可选，默认为true，对象是否被复制。
4.	order C(按行)、F(按列)或A(任意，默认)。
5.	subok 默认情况下，返回的数组被强制为基类数组。 如果为true，则返回子类。
6.	ndimin 指定返回数组的最小维数。
'''
a = np.array([1,2,3])
b = np.array([1,2,3], ndmin=2, )
c = np.array([1,2,3], dtype=complex)
print(a,'\n',b,'\n',c)
print(a.ndim,'\n',b.ndim,'\n',c.ndim)