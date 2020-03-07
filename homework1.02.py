#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:55:06 2020

@author: liwenxi
"""

def xiaoxiaole(text):
    stack = []
    for i in text:
        if stack == []:
            stack.append(i)
        else:
            if i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
    if stack == []:
        print("None")
    else:
        print( "".join(stack))


xiaoxiaole(input("请输入一串英文字符"))