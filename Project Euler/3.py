# -*- coding: utf-8 -*-
"""
Created on Fri May  4 19:02:01 2018

@author:Can Sevgi (github.com/CanSevgi)

We'll check for x%y==0 and y%z != 0 where y = (from x-1, to 0) and z = (from y-1, to 0)  
"""
x= 600851475143
#i=0
#n=0
#m=0
c=0
a=0

for c in range (1,10000,1):
    if x%c==0:
        a +=1
        print (a, " st. prime factor : " ,c)
        x= (x//c)
        print ("Result of the divide :",x)    
    
    
#for i in range (1,x,1):
#    if x%(x-i) ==0:
#        a = (x-i)
#        m=0
#        for n in range (2,a,1):
#            if (a)%(n)==0:
#                break
#            else :
#                m +=1
#        if m==(a-2) :
#            print (a)
#            break
                    
            