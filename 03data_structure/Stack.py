# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:01:12 2017

@author: U002ZXJ
"""

class Stack:
    def __init__(self):
        self.items =[]
        
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)