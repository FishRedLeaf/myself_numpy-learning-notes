# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:17:47 2018

@author: Administrator
"""

import numpy as np

'''
ndarray对象的内容可以通过索引或切片来访问和修改，就像 Python 的内置容器对象一样。
通过将start，stop和step参数提供给内置的slice函数来构造一个 Python slice对象。 
此slice对象被传递给数组来提取数组的一部分。
'''
a = np.arange(10)
#对一维数组进行切片slice
s = slice(2,7,2)
print(a[s],a[2:7:2])
print(a[5:]);print(a[5:8])
#对高维数组进行切片
b = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(b[1:])
'''
切片还可以包括省略号(...)，来使选择元组的长度与数组的维度相同。 
如果在行位置使用省略号，它将返回包含行中元素的ndarray
'''  
print(b[...,1]) #返回第二列元素的数组
print(b[1,...]) #返回第二行元素的数组
print(b[...,1:]) #返回第二列到最后一列元素的数组
print('\n')




'''以下为高级索引'''
'''如果一个ndarray是非元组序列，数据类型为整数或布尔值的ndarray，
或者至少一个元素为序列对象的元组，我们就能够用它来索引ndarray。
高级索引始终返回数据的副本。 与此相反，切片只提供了一个视图。
有两种类型的高级索引：整数和布尔值。
'''

'''
整数索引
这种机制有助于基于 N 维索引来获取数组中任意元素。 
每个整数数组表示该维度的下标值。 
当索引的元素个数就是目标ndarray的维度时，会变得相当直接。
'''
#example1
IntegerArray = np.array([[1,  2],  [3,  4],  [5,  6]])
X_search = [0,1,2] #行索引
Y_search = [0,1,0] #列索引 即寻找原数组中00 11 20处的元素
SegIntegerArray =  IntegerArray[X_search,Y_search]
print(IntegerArray);print(SegIntegerArray)
#example2
IntArray = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
rows1 = np.array([[0,0,3,3]]) 
cols1 = np.array([[0,2,0,2]]) 
SegIntArray = IntArray[rows1,cols1]
print(SegIntArray)
rows2 = np.array([[0,0],[3,3]]) 
cols2 = np.array([[0,2],[0,2]])
cols3 = np.array([[0,2]])
'''行索引和列索引若是多维的，那么切片生成的数组也将是多维的
[[(0,0),(0,2)],
 [(3,0),(3,2)]]
'''  
SubIntArray1 = IntArray[rows2,cols2]
SubIntArray2 = IntArray[rows2,cols3]
print(SubIntArray1);print(SubIntArray2)
print('\n')
'''
高级和基本索引可以通过使用切片:或省略号...与索引数组组合。 
以下示例使用slice作为列索引和高级索引。 当切片用于两者时，结果是相同的。 
但高级索引会导致复制，并且可能有不同的内存布局
'''
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
#y = x[[1,2,3],[1,2]]
y1 = x[1:4,[1,2]]
y2 = x[[1,2,3],1:3]
y3 = x[1:4,1:3]
y4 = x[[[1,1],[2,2],[3,3]],[[1,2],[1,2],[1,2]]]
print(y1);print(y2);print(y3);print(y4);
'''结论就是 使用slice切片较简单'''
'''
Q:y = x[[1,2,3],[1,2]]会导致IndexError,行索引3个元素，列索引两个元素
SubIntArray2 = IntArray[np.array([[0,0],[3,3]]) ,np.array([[0,2]])]无错误，
因为行索引两个元素，每个元素同时又是一维数组，列索引两个元素，每个元素都是一个常数，但仍然可以匹配
得出结论：进行切片时，只要数组[]内的行索引和列索引的行数相等即可。
[[0,0],[3,3]]：2*2  [0,2]：2*1
'''



'''
布尔索引
当结果对象是布尔运算(例如比较运算符)的结果时，将使用此类型的高级索引
'''
arr1 = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(arr1);print(arr1[x>5])
arr2 = np.array([np.nan,1,2,np.nan,3,4,5])  
print(arr2[~np.isnan(arr2)]) #排除数组中的nan，np.nan通俗讲是float类型的none
comp = np.array([1,  2+6j,  5,  3.5+5j])  
print(comp[np.iscomplex(comp)])







