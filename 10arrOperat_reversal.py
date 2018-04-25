# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:12:46 2018

@author: Administrator
翻转操作
1.	transpose 翻转数组的维度
2.	ndarray.T 和self.transpose()二维及以下作用相同
3.	rollaxis 向后滚动指定的轴
4.	swapaxes 互换数组的两个轴
"""

import numpy as np

'''
numpy.transpose(arr, axes) (arr为一维和二维时)效果等同于 arr.T(不适用于三维及以上)
这个函数翻转给定数组的维度。如果可能的话它会返回一个视图
arr：要转置的数组
axes：整数的列表，对应维度，通常所有维度都会翻转。

numpy.rollaxis(arr, axis, start)
该函数向后滚动特定的轴，直到一个特定位置
arr：输入数组
axis：要向后滚动的轴，其它轴的相对位置不会改变
start：默认为零，表示完整的滚动。会滚动到特定位置。

numpy.swapaxes(arr, axis1, axis2)
该函数交换数组的两个轴
arr：要交换其轴的输入数组
axis1：对应第一个轴的整数
axis2：对应第二个轴的整数
'''
a = np.arange(12).reshape(3,4)
b = np.transpose(a)
print(a);print(a.T);print(b)
x = np.arange(8).reshape(2,2,2)
print('\n');print(x);
print('\n');print(np.transpose(x,[1,0,2])) #可以通过一个正方体的三维坐标理解 z轴y轴x轴
print('\n');print(np.swapaxes(x,0,1))
print('\n');print(np.rollaxis(x,2,1))

'''
np.transpose(x,[1,0,2])完全给定了不同轴之间的交换顺序
假设数组x原来的轴的顺序是z轴y轴x轴
np.rollaxis(x,0) 轴的顺序由zyx变为yzx
np.rollaxis(x,1) 轴的顺序由zyx变为zxy
np.rollaxis(x,2) 轴的顺序由zyx变为xzy
np.rollaxis(x,2,1) 轴的顺序由zyx变为zxy
np.rollaxis(x,2,2) 轴的顺序由zyx变为zyx(不变)
关键一点在于除了那个滚动的轴，剩余的轴顺序不变
(x,1) zyx->zxy y向后滚动一个位置,但是z和x的位置关系不变
(x,2) zyx->xzy x向后滚动一个位置，但是后面没位置，故循环地放到z的前面，且y和x的位置关系不变
'''