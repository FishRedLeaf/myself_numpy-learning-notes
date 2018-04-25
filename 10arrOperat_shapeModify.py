# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:18:07 2018

@author: Administrator
修改形状
1.	reshape 不改变数据的条件下修改形状
2.	flat 数组上的一维迭代器
3.	flatten 返回折叠为一维的数组副本
4.	ravel 返回连续的展开数组
ravel & faltten
两者所要实现的功能是一致的（将多维数组降位一维）
两者的区别在于返回拷贝（copy）还是返回视图（view）
numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响（reflects）原始矩阵，
而numpy.ravel()返回的是视图（view，也颇有几分C/C++引用reference的意味），会影响（reflects）原始矩阵。
"""

import numpy as np

'''
numpy.reshape(arr, newshape, order) numpy.ndarray.reshape(newshape,order)
在不改变数据的条件下修改形状
arr：要修改形状的数组
newshape：整数或者整数数组，新的形状应当兼容原有形状
order：'C'为 C 风格顺序，'F'为 F 风格顺序，'A'为保留原顺序。

numpy.ndarray.flat
返回数组上的一维迭代器，行为类似 Python 内建的迭代器
numpy.ndarray.flatten(order) #order决定C风格还是F风格展开，即按行展开按列展开
返回折叠为一维的数组副本

numpy.ravel(arr,order) numpy.ndarray.ravel(order)
返回展开的一维数组，并且按需生成副本
'''
a = np.arange(8);print(a)
b = a.reshape([2,4])
c = np.reshape(a,[2,4])
print(b);print(c)
b_flat = b.flat;print(b_flat);print(b_flat[2])
b_flatten = b.flatten(order = 'F');print(b_flatten);print(b_flatten[2])
b_Cravel = b.ravel();b_Fravel = b.ravel(order = 'F')
print(b_Cravel);print(b_Fravel)