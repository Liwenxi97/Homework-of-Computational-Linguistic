#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:35:29 2020

@author: liwenxi
"""
"""给定一个M进制的数，请将其转换为N进制并输出"""
M = int(input("请输入转换数字的进制数"))
N = int(input("请输入要转换的进制数"))
number = input("请输入要转换的数字")
digit = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
def toTen(number, M):
    tenNum = 0
    for i in number:
        tenNum = tenNum + int(i) * M ** (len(number)-number.index(i)-1)
    return tenNum

def toN(number, N):
    if int(number) < N:
        return digit[int(number)]
    else:
        return toN(int(number)//N, N) + digit[int(number)%N]
    
print(toN(toTen(number,M), N))

"""如课上所说，汉诺塔问题源于印度一个古老传说。对于原始的汉诺塔游戏，可供玩家操作的空间一共
只有三根柱子，导致按原传说的要求，需要超过1.8*10^19步才能解开。通过新增柱子可以大幅度地减
少需要的步数。此处要求在给出指定的盘数，柱子数量为4（即限制为4根柱子）且不改变原有传说的其他
规则的限制下，找出完成迁移的最小步骤。"""
 
def movethreeTower(height, firTower, secTower, thiTower):
    if height >= 1:
        movethreeTower(height-1, firTower, thiTower, secTower)
        moveDisk(height, firTower, thiTower)
        movethreeTower(height-1, secTower, firTower, thiTower)

def moveDisk(height, firTower, thiTower):
    print(f"move disk[{height}] from {firTower} to {thiTower}")

def towerOfHanoi(n, from_rod, to_rod, aux_rod1, aux_rod2): 
    if (n == 0): 
        return
    if (n == 1): 
        print("Move disk", n, "from rod",  
                 from_rod, "c to rod",  to_rod) 
        return
      
    towerOfHanoi(n - 2, from_rod, aux_rod1, aux_rod2, to_rod) 
    print("Move disk", n-1, "from rod", from_rod, "c to rod", aux_rod2) 
                  
    print("Move disk", n, "from rod", from_rod, "c to rod", to_rod) 
                  
    print("Move disk", n-1, "from rod", aux_rod2, "c to rod", to_rod) 
              
    towerOfHanoi(n - 2, aux_rod1, to_rod, from_rod, aux_rod2) 
        
towerOfHanoi(4, "#1", "#2", "#3","#4")

 
"""谢尔宾斯基地毯是形如上图的正方形分形图案，每个地毯可分为等大小的9份，其中中央挖空，其余均
由更小的地毯组成。现给定地毯大小（行数）与组成地毯的字符元素，请打印相应的地毯图形。
注：空腔以半角空格表示；当给定字符元素长度不为1时空格数须与字符长度对应"""
         
def sierpinski_carpet(n):
  carpet = ["()"]
  for i in range(n):
    carpet = [x + x + x for x in carpet] + \
    [x + x.replace("()","  ") + x for x in carpet] + \
    [x + x + x for x in carpet]
    print(carpet)
  return "\n".join(carpet)
 
print(sierpinski_carpet(2))
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             