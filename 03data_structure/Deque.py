# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:12:51 2017

@author: U002ZXJ
"""

class Deque:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def add_front(self,item):
        self.items.append(item)
    
    def add_rear(self,item):
        self.items.insert(0,item)
    
    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)