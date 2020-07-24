#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:32:08 2020

@author: kmi20042005
"""

#Given an array of integers, return a new array such that the element at index i
#is the product of all the numbers in the array except the one at i
#don't use division

#I previously solved this as an email challenge 
#see Kat-and-Tom-Code-Challenge #2

#the book suggest a more elegant solution which I have implemented here
#"generate a list of prefix products and suffix products" 

def listproduct(x):
    
    prefix=[1]
    suffix=[1]
    product=[]
    
    for i in range(0,len(x)-1):
        prefix.append(prefix[-1]*x[i])
        suffix.append(suffix[-1]*x[-i-1])
        
    for i in range(0,len(x)):
        product.append(prefix[i]*suffix[-i-1])

    return product

#old code from challenge #2 to compare
def mult_array2(a):
    
    #b is the resulting array 
    b=[]
    
    #iterate over each number 
    for i in range(0,len(a)):
        
        #c will be the multiplied value
        c=1
        
        #remove value at i and save for later
        ai=a.pop(0)
        
        #iterate over remaining values to multiply
        for i in range(0,len(a)):
            c=c*a[i]
        
        #add to the array 
        b.append(c)
        
        #add removed value back in at the end of the array 
        a.append(ai)
        
    return b
