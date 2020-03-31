#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:45:21 2020

@author: liwenxi
"""
'''给定一个只包括'('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。

有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

输入格式:
一行字符串

输出格式：
True或False，表示该输入是否为合法括号串'''

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
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    