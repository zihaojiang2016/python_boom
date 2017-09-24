# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 12:53:27 2017

@author: U002ZXJ
"""
from turtle import *

def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')        
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()
