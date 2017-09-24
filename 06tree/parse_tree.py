# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:13:16 2017

@author: U002ZXJ
"""

import Stack, binary_tree

def build_parse_tree(fp_exp):
    fp_list = fp_exp.split()
    p_stack = Stack.Stack()
    e_tree = binary_tree.BinaryTree('')
    p_stack.push(e_tree)
    current_tree = e_tree
    for i in fp_list:
        if i == '(':
            current_tree.insert_left('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i not in ['+','-','*','/',')']:
            current_tree.set_root_val(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i in  ['+','-','*','/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            p_stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ')':
            current_tree = p_stack.pop()
        else:
            raise ValueError
    
    return current_tree
 
import operator

def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub,'*': operator.mul,'/': operator.truediv}
    
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()
    
    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(int(evaluate(left)),int(evaluate(right)))
    else:
         return parse_tree.get_root_val()
     

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        preorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

def print_exp(tree):
    str_val =  ""
    if tree:
        left = tree.get_left_child()
        right = tree.get_right_child() 
        if left and right:
            str_val = '(' + print_exp(left)
            str_val = str_val + str(tree.get_root_val())
            str_val = str_val + print_exp(right) + ')'
        else:
            str_val = print_exp(left)
            str_val = str_val + str(tree.get_root_val())
            str_val = str_val + print_exp(right)
    return str_val


    
preorder(pt)
postorder(pt)
inorder(pt)

print(print_exp(pt))

