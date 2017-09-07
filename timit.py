# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:50:49 2017

@author: U002ZXJ
"""

class Stack:
    def __init__(self):
        self.items = []
        
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
    
def checker(x):
    a = Stack()
    balanced = True
    index = 0
    while index < len(x) and balanced:
        i = x[index]
        if i == "(":
            a.push(i)
        else:
            if a.is_empty():
                balanced = False
            else:
                a.pop()
        index += 1
    if balanced and a.is_empty():
        return True
    else:
        return False
    
    
    