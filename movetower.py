# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def move_disk(fp,tp):
    print("moving disk from ",fp," to ", tp)
    
def move_tower(h,from_pole,to_pole,with_pole):
    if h >= 1:
        move_tower(h-1,from_pole,with_pole,to_pole)
        move_disk(from_pole,to_pole)
        move_tower(h-1,with_pole,to_pole,from_pole)
        
