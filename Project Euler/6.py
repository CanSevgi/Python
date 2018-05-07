# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:50:11 2018

@author:Can Sevgi (github.com/CanSevgi)
"""
sam = 0
sqsam=0
i=0
for i in range(1,101,1):
    sqsam+= (i**2)
    sam += i
print ((sam**2)-sqsam)

#07.05.2018 22:51