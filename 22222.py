# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:31:48 2018

@author: thrialgorithm
"""
import sympy
import numpy as np
import math
import xlrd
wb = xlrd.open_workbook(r'F:\python_files\LocationPosintioning.xls')
sh = wb.sheet_by_index(0)
nu1_column = sh.col_values(0)
nu2_column = sh.col_values(1)
nu3_column = sh.col_values(2)
nu4_column = sh.col_values(3)
loc_column = sh.col_values(4)
print(nu1_column)
print(nu2_column)
print(nu1_column[4])

for i in range(1,14):
    print(nu1_column[i])
def triposition(pow1,pow2,pow3,pow4,power1,power2,power3,power4):
    f1 = math.sqrt(np.square(pow1-power1)+np.square(pow2-power2)+np.square(pow3-power3)+np.square(pow4-power4))
    return f1

#LocPower = np.random.rand(4)
'''list1=[]
str1 = input("请输入数值，用，隔开：")
list2 = str1.split(",")
i =0
while i <=4:
    list1.append(int(list2.pop()))
    i += 1
print(list1)'''
str1 = input("请输入数值，用，隔开：")
PowerNum1,PowerNum2,PowerNum3,PowerNum4 = str1.split(',')
x=int(PowerNum1)
y=int(PowerNum2)
z=int(PowerNum3)
w=int(PowerNum4)
print(x,y,z,w)

list = []
for i in range(1,14):
     print(triposition(x,y,z,w,nu1_column[i],nu2_column[i],nu3_column[i],nu4_column[i]))#三边定位算法的结果
     list.append(triposition(x,y,z,w,nu1_column[i],nu2_column[i],nu3_column[i],nu4_column[i]))
aa = min(list)
num_index = list.index(aa)
print(min(list))
print(num_index)
print(loc_column[num_index+1])
print(list.index(min(list)))    