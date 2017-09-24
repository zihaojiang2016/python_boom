# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:24:05 2017

@author: U002ZXJ
"""

def factorial(number):
    if number <= 1:
        return 1
    else:
        return factorial(number-1)*number
    
print(factorial(10))