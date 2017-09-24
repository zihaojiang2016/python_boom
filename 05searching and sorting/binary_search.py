# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:22:56 2017

@author: U002ZXJ
"""

def binary_search(a_list,item):
    start = 0
    end = len(a_list)-1
    found = False
    while start <= end and not found:
        middle = (start + end)//2
        if a_list[middle] == item:
            found = True
        else:
            if a_list[middle]<item:
                start = middle+1
            else:
                end = middle -1
    return found



def bin_search_recur(a_list,item):
    start = 0
    end = len(a_list)-1
    middle = (start + end)//2
    if start >= end:
        return a_list[middle] == item
    else:
        if a_list[middle]<item:
            return bin_search_recur(a_list[middle+1:],item)
        else:
            return bin_search_recur(a_list[:middle-1],item)

def bin_search_recur_answer(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        middle = len(a_list)//2
    if a_list[middle] == item:
        return True
    else:
        if a_list[middle] > item:
            return bin_search_recur_answer(a_list[:middle],item)
        else:
            return bin_search_recur_answer(a_list[middle+1:],item)
        

