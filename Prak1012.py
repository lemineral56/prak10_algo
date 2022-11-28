#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:34:25 2022

@author: rhenatabella
"""

def a(x):
    for i in range(len(x)-1,0,-1):
        for j in range(i):
            if x[j]>x[j+1]:
                temp = x[j]
                x[j]=x[j+1]
                x[j+1]=temp
data = [9,8,-2,1,3,4,5]
a(data)
print("List yang sudah disorting")
print(data)