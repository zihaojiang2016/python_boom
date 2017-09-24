# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:04:48 2017

@author: U002ZXJ
"""

import Stack

def divided_by_2(dec_number):
    rem_st = Stack.Stack()
    
    while dec_number > 0:
        rem = dec_number % 2
        rem_st.push(rem)
        dec_number = dec_number//2
        
    bin_str = ""
    while not rem_st.is_empty():
        bin_str += str(rem_st.pop())
    
    return bin_str

