# -*- coding: utf-8 -*-
"""
Created on Mon May  7 21:04:59 2018

@author:Can Sevgi (github.com/CanSevgi)

Task :
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
hcs=0
x=999
y=999
i=0
a=0
k=0
n=0
z=0
s=""
for i in range(0,900,1):
    for k in range(0,900,1):
        z=(x-i)*(y-k)
        s=str(z)
        a=len(s)
        n=0
        for j in range(a//2):
            if s[j]==s[a-1-j]:
                n+=1
            else:
                break
        if n==(a//2):
            if z>hcs:
                hcs = z
print (hcs)
        
#07.05.2018 21:37
