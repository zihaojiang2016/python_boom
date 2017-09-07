# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 22:46:16 2017

@author: U002ZXJ
"""

import Stack

def infix_to_postfix(infix_expr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3 
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    op_stack = Stack.Stack()
    postfix = []
    token_list = infix_expr.split()
    
    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ012345678":
            postfix.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            aa = op_stack.pop()
            while aa != "(":
                postfix.append(aa)
                aa = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and prec[op_stack.peek()] >= prec[token]:
                postfix.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix.append(op_stack.pop())
    return " ".join(postfix)

def do_math(op,op1,op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2   
    
    
def postfix_eval(postfix_expr):
    oprand_stack = Stack.Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            oprand_stack.push(int(token))
        else:
            op2 = oprand_stack.pop()
            op1 = oprand_stack.pop()
            result = do_math(token,op1,op2)
            oprand_stack.push(result)
    return oprand_stack.pop()