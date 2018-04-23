# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:31:56 2018

@author: Administrator
"""

import numpy as np

'''
numpy.asarray(a, dtype = None, order = None)
类似于numpy.array，但具有较少的参数
1.	a 任意形式的输入参数，比如列表、列表的元组、元组、元组的元组、元组的列表
2.	dtype 通常，输入数据的类型会应用到返回的ndarray
3.	order 'C'为按行的 C 风格数组，'F'为按列的 Fortran 风格数组
'''
#来自列表的 ndarray
a = [1,2,3]
x1 = np.asarray(a);print(x1)
x2 = np.asarray(a,dtype = float);print(x2)
#来自元组的 ndarray
b = (1,2,3)
x11 = np.asarray(b);print(x11)
x22 = np.asarray(b,dtype = float);print(x22)
#来自元组列表的 ndarray
c =  [(1,2,3),(4,5)] 
x111 = np.asarray(c) ;print(x111)

'''
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
此函数将缓冲区解释为一维数组
1.	buffer 任何暴露缓冲区借口的对象
2.	dtype 返回数组的数据类型，默认为float
3.	count 需要读取的数据数量，默认为-1，读取所有数据
4.	offset 需要读取的起始位置，默认为0
'''
#A byte string is a fixed-length array of bytes. 
#A byte is an exact integer between 0 and 255 inclusive.
s =  b'Hello World' #byte string
y = np.frombuffer(s, dtype =  'S1');print(y) 

'''
numpy.fromiter(iterable, dtype, count = -1)
此函数从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组
1.	iterable 任何可迭代对象
2.	dtype 返回数组的数据类型
3.	count 需要读取的数据数量，默认为-1，读取所有数据
''' 
lyst = range(5)
it = iter(lyst) #从列表中获得迭代器
z = np.fromiter(it, dtype =  float)  
print(z)
