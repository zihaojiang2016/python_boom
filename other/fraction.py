# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 09:21:03 2017

@author: U002ZXJ
"""
def gcd(m,n):
    while m % n != 0:
        old_m = m
        old_n = n
        
        m = old_n
        n = old_m % old_n
        
    return n


class Fraction:
    def __init__(self,top,bottom):
        if isinstance(top,int):
            self.num = top
        else:
            raise ValueError("top is not an int")
        
        if isinstance(bottom,int):
            self.den = bottom
        else:
            raise ValueError("bottom is not an int")
        
        common = gcd(top,bottom)
        self.num = self.num // common
        self.den = self.den // common
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,other):
        if type(other) == int:
            other = Fraction(other,1)
        if type(other) == float:
            other = Fraction(other.as_integer_ratio()[0],other.as_integer_ratio()[1])
   
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num,new_den)
            
        return Fraction(new_num // common, new_den // common)
   
    def __iadd__(self,other):
        return self.__add__(other)
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __eq__(self,other):
        c1 = self.num * other.den
        c2 = self.den * other.num
        
        return c1 == c2
    
    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num,new_den)
        
        return Fraction(new_num // common, new_den // common)
    
    def __sub__(self,other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num,new_den)
        
        return Fraction(new_num // common, new_den // common)
    
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num,new_den)
        
        return Fraction(new_num // common, new_den // common)
    
    def get_num(self):
        return self.num
    
    def get_den(self):
        return self.den
    
    def __gt__(self,other):
        c1 = self.num * other.den
        c2 = self.den * other.num
        
        return c1 > c2
    
    def __ge__(self,other):
        c1 = self.num * other.den
        c2 = self.den * other.num
        
        return c1 >= c2
    
    def __lt__(self,other):
        c1 = self.num * other.den
        c2 = self.den * other.num
        
        return c1 < c2
    
    def __le__(self,other):
        c1 = self.num * other.den
        c2 = self.den * other.num
        
        return c1 <= c2
    
    def __ne__(self,other):
        c1 = self.num * other.den
        c2 = self.den * other.num
        
        return c1 != c2
    
    
    
    
    
    
    
    
    
    
    
    
    