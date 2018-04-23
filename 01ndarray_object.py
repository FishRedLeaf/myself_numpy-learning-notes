# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:57:34 2018

@author: Administrator
"""

import numpy as np

'''
numpy.dtype(object, align, copy)
参数
Object：被转换为数据类型的对象。
Align：如果为true，则向字段添加间隔，使其类似 C 的结构体。
Copy： 生成dtype对象的新副本，如果为false，结果是内建数据类型对象的引用。

每个内建类型都有一个唯一定义它的字符代码:
'b'：布尔值
'i'：符号整数
'u'：无符号整数
'f'：浮点
'c'：复数浮点
'm'：时间间隔
'M'：日期时间
'O'：Python 对象
'S', 'a'：字节串
'U'：Unicode
'V'：原始数据(void)
'''

dt = np.dtype(np.int32)  
print(dt)

#int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。  
dt2 = np.dtype('i4')
print(dt2)
dt3 = np.dtype('>i4')
print(dt3)

#创建结构化数据类型,并将其应用于ndarray对象
dt4 = np.dtype([('age',np.int8)])  
print(dt4)
a = np.array([(10,),(20,),(30,)], dtype = dt4)
print(a)
print(a['age']) #文件名称'age'可用于访问 age 列的内容 

student = np.dtype([('name','S20'),  ('age',  'i1'),  ('marks',  'f4')]) 
studentArray = np.array([('lifeng',  23,  59.9),('buwei',  23,  99)], dtype = student)  
print(studentArray)