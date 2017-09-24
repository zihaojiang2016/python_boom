# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 15:57:22 2017

@author: U002ZXJ
"""

import Deque


def pal_checker(a_string):
    str_deq = Deque.Deque()
    
    for i in a_string:
        str_deq.add_rear(i)
    
    still_equal = True
    
    while still_equal and str_deq.size()>1:
        front = str_deq.remove_front()
        rear = str_deq.remove_rear()
        if rear != front:
            still_equal = False
        
    return still_equal

        