# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:55:05 2018

@author: Administrator
"""
import numpy as np

'''
数组属性
shape 
获得数组的大小，也可以通过给shape赋值修改原数组的大小
reshape 
原数组的一个副本修改大小，并返回一个新数组
ndim 
返回数组的维数 判别维数,可以看方括号，或者生成数组时的ndmin值
itemsize 
返回数组中每个元素的字节单位长度,根据ditype的类型，如int8一个字节，float32四个字节
flags：
1.	C_CONTIGUOUS(C) 数组位于单一的、C 风格的连续区段内
2.	F_CONTIGUOUS(F) 数组位于单一的、Fortran 风格的连续区段内
3.	OWNDATA(O) 数组的内存从其它对象处借用
4.	WRITEABLE(W) 数据区域可写入。 将它设置为flase会锁定数据，使其只读
5.	ALIGNED(A) 数据和任何元素会为硬件适当对齐
6.	UPDATEIFCOPY(U) 这个数组是另一数组的副本。当这个数组释放时，源数组会由这个数组中的元素更新
'''
a = np.array([[1,2,3],[4,5,6],[7,8,9],[11,22,33]])
print('原始数组a：',a)
a.shape = (2,6) #改变原数组
print('shape赋值后的数组a：',a)
b = a.reshape(6,-1) #改变原数组副本，reshape不改变原数组
print('reshape作用于数组a得到的数组b：',b)
print('shape和reshape后的数组a：',a)
print('数组a和数组b的维数：',a.ndim,b.ndim) #a:2*6 b:6*2
c = np.array([[1],[1],[1],[1],[1],[1],[1],[1]])
print('数组c：',c,'数组c的维数',c.ndim)
print('数组a中每个元素的字节长度：',a.itemsize,'\n','数组a中每个元素的类型：',type(a[0][0]))
print(a.flags)