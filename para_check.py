# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:01:15 2017

@author: U002ZXJ
"""

import Stack


def matches(op,cl):
    opens = '([{'
    closes = ')]}'
    return opens.index(op) == closes.index(cl)

    
def checker(x):
    s = Stack()
    balanced = True
    index = 0
    while index < len(x) and balanced:
        sym = x[index]
        if sym in "([{":
            s.push(sym)
        else:
            if s.is_empty():
                return False
            else:
                top = s.pop()
                if not matches(top,sym):
                    return False
        index += 1
        
    if balanced and s.is_empty():
        return True
    else:
        return False