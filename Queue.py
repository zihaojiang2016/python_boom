# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:52:48 2017

@author: U002ZXJ
"""

class Queue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
    
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)