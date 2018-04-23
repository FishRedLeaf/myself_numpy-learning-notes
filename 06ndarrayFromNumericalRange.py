# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:20:21 2018

@author: Administrator
"""

import numpy as np

'''
numpy.arange(start, stop, step, dtype)
这个函数返回ndarray对象，包含给定范围内的等间隔值。
1.	start 范围的起始值，默认为0
2.	stop 范围的终止值(不包含)
3.	step 两个值的间隔，默认为1
4.	dtype 返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型。
'''

x1 = np.arange(5);print(x1)
x2 = np.arange(5, dtype = float);print(x2)
x3 = np.arange(1,10,2);print(x3)

'''
numpy.linspace(start, stop, num, endpoint, retstep, dtype)
在此函数中，指定了范围之间的均匀间隔数量，而不是步长
1.	start 序列的起始值
2.	stop 序列的终止值，如果endpoint为true，该值包含于序列中
3.	num 要生成的等间隔样例数量，默认为50
4.	endpoint 序列中是否包含stop值，默认包含，即endpoint=true
5.	retstep 如果为true，返回样例，以及连续数字之间的步长
6.	dtype 输出ndarray的数据类型
'''
y1 = np.linspace(1,10,5);print(y1)
y2 = np.linspace(1,10,5, endpoint = False);print(y2)
y3, step= np.linspace(1,10,5, retstep = True);print(y3, step)

'''
numpy.logspace(start, stop, num, endpoint, base, dtype)
此函数返回一个ndarray对象，其中包含在对数刻度上均匀分布的数字。 
刻度的开始和结束端点是某个底数的幂，通常为 10。
1.	start 起始值是base ** start(base^start)
2.	stop 终止值是base ** stop(base^stop)
3.	num 范围内的数值数量，默认为50
4.	endpoint 如果为true，终止值包含在输出数组当中
5.	base 对数空间的底数，默认为10
6.	dtype 输出数组的数据类型，如果没有提供，则取决于其它参数
'''
z1 = np.logspace(1,2,10);print(z1)
z2 = np.logspace(1,10,num=10,base=2);print(z2)



