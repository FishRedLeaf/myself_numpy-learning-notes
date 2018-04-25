# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:55:08 2018

@author: Administrator
1.	broadcast 产生模仿广播的对象
2.	broadcast_to 将数组广播到新形状
3.	expand_dims 扩展数组的形状
4.	squeeze 从数组的形状中删除单维条目
"""

import numpy as np

'''
broadcast(arr1,arr2)
NumPy内置了对广播的支持,此功能模仿广播机制。 
它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。

iter()函数获取这些可迭代对象的迭代器
对获取到的迭代器不断使用next()函数来获取下一条数据 next(b) 注意np.broadcast(x,y)返回的就是迭代器

numpy.broadcast_to(array, shape, subok)
此函数将数组广播到新形状。 它在原始数组上返回只读视图。 它通常不连续。
如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError。

numpy.expand_dims(arr, axis)
函数通过在指定位置插入新的轴来扩展数组形状
arr：输入数组
axis：新轴插入的位置

numpy.squeeze(arr, axis) 与expand_dims相反的操作
函数从给定数组的形状中删除一维条目
arr：输入数组
axis：整数或整数元组，用于选择形状中单一维度条目的子集
'''
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
# 对 y 广播 x
b = np.broadcast(x,y);print('b的shape：',b.shape) 
# 它拥有 iterator 属性，基于自身组件的迭代器元组
print('b的内容：')
for s in b:
    print(s)

b = np.broadcast(x,y)
c = np.zeros(b.shape);print('c的shape：',c.shape);print('c:',c)
print('手动使用 broadcast 将 x 与 y 相加：')
c.flat = [u + v for (u,v) in b]
print(c);print('numpy内置的广播将 x 与 y 相加：');print(x+y)

a = np.arange(4)
b = a.reshape(1,4)
print('对a和b调用 broadcast_to 函数之后：')
print(np.broadcast_to(a,(4,4)))
print(np.broadcast_to(b,(4,4)))

x = np.array(([1,2],[3,4]))
y0 = np.expand_dims(x, axis = 0)
y1 = np.expand_dims(x, axis = 1)
y2 = np.expand_dims(x, axis = 2)
print(x);print(y0);print(y1);print(y2)
print(x.shape);print(y0.shape);print(y1.shape);print(y2.shape)

print('\n')
x = np.arange(9).reshape(1,3,3)
y = np.squeeze(x)
print(x);print(y)
print(x.shape);print(y.shape)






