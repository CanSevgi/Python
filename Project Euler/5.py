# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:56:51 2018

@author:Can Sevgi (github.com/CanSevgi)
"""
n=0
a=0
x=2
for i in range(1,20,1):
    if x%i!=0:
        a=i
        for n in range (1,(i),1):
            if a%n==0:
                a=(a//n)
        x=(x*a)
print (x)

#07.05.2018 22:20