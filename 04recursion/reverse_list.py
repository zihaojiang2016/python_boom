# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 12:27:23 2017

@author: U002ZXJ
"""

def reverse_list(list_in):
    if len(list_in) <= 1:
        return list_in
    else:
        a = reverse_list(list_in[1:])
        b = list_in[0]
        a.append(b)
        return a
    
print(reverse_list([3,4,6,7,5]))