#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:45:21 2020

@author: liwenxi
"""
"""给定一个只包括
 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
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
"""
开心消消乐我们都熟悉，我们可以用刚学过的栈来做一个“一维”的开心消消乐游戏，这个游戏输入一串字符，逐个消去相邻的相同字符对。
如果字符全部被消完，则输出不带引号的“None”
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


"""
洗碗工小明碰上了一位强迫症老板老王，餐厅一共就10只盘子，老板给仔细编上了0～9等10个号码，并要求小明按照从0到9的编号来洗盘子，当然，每洗好一只盘子，就必须得整齐叠放起来。
小明洗盘子期间，经常就有顾客来取盘子，当然每位顾客只能从盘子堆最上面取1只盘子离开。
老王在收银台仔细地记录了顾客依次取到盘子的编号，比如“1043257689”，这样他就能判断小明是不是遵照命令按照0123456789的次序来洗盘子了。
你也能像老王一样作出准确的判断吗？
输入格式:
长度为10的字符串，其中只包含0～9的数字，且不重复，代表顾客依次取到的盘子编号
输出格式：
字符串：Yes或者No，表示遵照次序洗盘子，或者没有遵照次序洗盘子
"""
num=input("请输入你的值：")

sign=0 #记录每一次被比较的前一个数字
yesno=0
ti=0 #记录每一个需要比较的后一个数字数字的索引值
for i in num: 
    if int(i)<sign: #若后一个数小于前一个数需要作出判断，大于则不想要
        de=sign-int(i)
        testList=[j for j in num[ti+1:] if int(j) < sign] #找到所有小于被比较的前一个数的数
        for k in testList:
            if sign-int(k) < de: #后一个数字应是小于前一个数里最大的那个
                yesno=1
    sign=int(i)
    ti=ti+1
    
if yesno==1:
    print("NO")
else:
    print("YES")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
