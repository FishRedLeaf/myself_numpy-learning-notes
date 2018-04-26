# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:09:31 2018

@author: Administrator
数组分割
1.	split 将一个数组分割为多个子数组
2.	hsplit 将一个数组水平分割为多个子数组(按列)
3.	vsplit 将一个数组竖直分割为多个子数组(按行)
"""

import numpy as np

'''
numpy.split(arr, indices_or_sections, axis)
arr：被分割的输入数组
indices_or_sections：可以是整数，表明要从输入数组创建的，等大小的子数组的数量。 
如果此参数是一维数组，则其元素表明要创建新子数组的点。
axis：默认为 0

numpy.hsplit是split()函数的特例，其中轴为 1 表示水平分割，无论输入数组的维度是什么

numpy.vsplit是split()函数的特例，其中轴为 0 表示竖直分割，无论输入数组的维度是什么

numpy.dsplit函数使用的是面向深度的分割方式
'''

a = np.arange(9);print(a)
b1 = np.split(a,3);print(b1) #分成三段，指定的数值(如3)必须整除len(a)
b2 = np.split(a,[4,7]);print(b2) #表示在4 7 对应的位置处进行分割

a1 = np.arange(16).reshape(4,4);print(a1)
c1 = np.hsplit(a1,2);print(c1)
c2 = np.vsplit(a1,2);print(c2)

a2 = np.arange(16).reshape(2,2,4);print(a2)
c3 = np.dsplit(a2,2);print(c3)