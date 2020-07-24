#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:27:27 2020

@author: kmi20042005
"""
from onepone import mult_array2, listproduct
import time 
import matplotlib.pyplot as plt

lptime=[]
matime=[]

for i in range(0,1000,10):
    x=list(range(0,i))
    
    t1=time.process_time()
    mult_array2(x)
    t2=time.process_time()
    
    t3=time.process_time()
    listproduct(x)
    t4=time.process_time()
    
    lptime.append(t4-t3)
    matime.append(t2-t1)
    
plt.plot(range(0,1000,10),lptime,'ro')
plt.plot(range(0,1000,10),matime,'bx')