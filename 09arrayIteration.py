# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 10:31:07 2018

@author: Administrator

NumPy 包包含一个迭代器对象numpy.nditer。 
它是一个有效的多维迭代器对象，可以用于在数组上进行迭代。 
数组的每个元素可使用 Python 的标准Iterator接口来访问
numpy.nditer(可迭代对象,order,op_flags)
op_flags must be a tuple or array of per-op flag-tuples
flags参数，可接受下列值：
1.	c_index 可以跟踪 C 顺序的索引
2.	f_index 可以跟踪 Fortran 顺序的索引
3.	multi-index 每次迭代可以跟踪一种索引类型
4.	external_loop 给出的值是具有多个值的一维数组，而不是零维数组

iter()函数获取可迭代对象的迭代器 iter(lyst)
"""
import numpy as np
a = np.arange(0,60,5) 
a = a.reshape(3,4)
print('a:');print(a)
print('a的迭代：')
for x in np.nditer(a):
    print(x)

'''迭代的顺序匹配数组的内容布局，而不考虑特定的排序。 这可以通过迭代上述数组的转置来看到'''
b = a.T
print('\n');print('a.T的迭代：')
for x in np.nditer(b):
    print(x)
    
'''如果相同元素使用 F 风格顺序存储，则迭代器选择以更有效的方式对数组进行迭代'''
c = b.copy(order = 'C')
print('\n');print('a.T(C风格)的迭代：')
for x in np.nditer(c):
    print(x)
print('\n');print('a.T(F风格)的迭代：')
d = b.copy(order = 'F')
for x in np.nditer(d):
    print(x)
    
'''可以通过显式提醒，来强制nditer对象使用某种顺序'''
print('\n');print('a.T(强制order=C)的迭代：')
for x in np.nditer(b,order = 'C'):
    print(x)
print('\n');print('a.T(强制order=F)的迭代：')
for x in np.nditer(b,order = 'F'):
    print(x)
    
'''nditer对象有另一个可选参数op_flags。 
其默认值为只读，但可以设置为读写或只写模式。 这将允许使用此迭代器修改数组元素'''
m = np.arange(0,60,5) 
m = m.reshape(3,4)
print('\n');print('初始数组m：');print(m)
for x in np.nditer(m, op_flags=['readwrite']): 
    x[...]=2*x 
print('\n');print('读写模式下各元素乘2的数组m：');print(m)
print('\n');print('external_loop标志下读取数组m：')
for x in np.nditer(m, flags =  ['external_loop'], order =  'F'):  
    print(x)

'''广播迭代'''
'''如果两个数组是可广播的，nditer组合对象能够同时迭代它们'''
n = np.array([1,  2,  3,  4], dtype =  int)
print('\n');print('n:');print(n)
print('数组n被广播到数组m的大小：')   
for x,y in np.nditer([m,n]):  
    print("%d:%d"  %  (x,y))

'''iter和np.nditer的区别，前者每一项都是可迭代对象中的元素，
后者每一项将原可迭代对象中的元素变为数组'''
lyst = [1,2,3,4]
lyst_iter = iter(lyst)
for s in lyst_iter:
    print(s)
lyst_nditer = np.nditer(lyst)
for s in lyst_nditer:
    print(s)
'''next()函数用于iter获得的迭代器可不断获得下一条元素
    next()函数用于np.nditer()函数获得的迭代器则直接输出整个迭代器的内容'''
lyst_iter = iter(lyst);print(next(lyst_iter))
lyst_nditer = np.nditer(lyst);print(next(lyst_nditer))