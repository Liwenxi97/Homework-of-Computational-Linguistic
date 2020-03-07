#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:45:21 2020

@author: liwenxi
"""


def test(Kuohao):
    stack = []
    for i in Kuohao:
        if i=="(" or i=="{" or i=="[":
            stack.append(i)
        if i ==")" and stack.pop() != "(":
            return False
        if i =="}" and stack.pop() != "{":
            return False
        if i =="]" and stack.pop() != "[":
            return False
    return True    


print(test(input("请输入一组括号")))
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    