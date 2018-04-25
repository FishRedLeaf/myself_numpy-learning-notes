# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 09:53:21 2018

@author: Administrator

1.	concatenate 沿着现存的轴连接数据序列
2.	stack 沿着新轴连接数组序列
3.	hstack 水平堆叠序列中的数组(列方向)
4.	vstack 竖直堆叠序列中的数组(行方向)
"""

import numpy as np

'''
numpy.concatenate((a1, a2, ...), axis)
沿指定轴连接相同形状的两个或多个数组
a1, a2, ...：相同类型的数组序列
axis：沿着它连接数组的轴，默认为 0

numpy.stack(arrays, axis)
此函数沿新轴连接数组序列
arrays：相同形状的数组序列
axis：返回数组中的轴，输入数组沿着它来堆叠

numpy.hstack(arrays)
numpy.stack函数的变体，通过堆叠来生成水平的单个数组
'''
a = np.array([[1,2,10,20],[3,4,30,40],[5,6,50,60]]);print('a:');print(a)
b = np.array([[7,8,70,80],[9,10,90,100],[11,12,110,120]]);print('b:');print(b)
print('沿轴axis=0连接a,b：');print(np.concatenate((a,b))) #按行连接，上面是a的各行，下面是b的各行
print('沿轴axis=1连接a,b：');print(np.concatenate((a,b),axis = 1)) #按列连接
x1 = np.stack((a,b));x2 = np.stack((a,b),axis=1);x3 = np.stack((a,b),axis=2)
print('沿轴axis=0 stack a,b：');print(x1)
print('沿轴axis=1 stack a,b：');print(x2)
print('沿轴axis=2 stack a,b：');print(x3)
print(x1.shape,x2.shape,x3.shape)

y = np.hstack((a,b));print(y)
z = np.vstack((a,b));print(z)