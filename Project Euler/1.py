# -*- coding: utf-8 -*-
"""
Created on Thu May  3 19:57:24 2018

@author:Can Sevgi (github.com/CanSevgi)
"""
sam =0
for i in range(1000):
    if (i%3==0) :
        sam +=i
    elif (i%5==0):
        sam+=i
print (sam)
