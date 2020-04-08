#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 09:44:34 2020

@author: liwenxi
"""

'''著名的快速排序算法里有一个经典的划分过程：我们通常采用某种方法取一个元素作为主元（中值），
通过交换，把比主元小的元素放到它的左边，比主元大的元素放到它的右边。 给定划分后的N个互不相同
的正整数的排列，请问有多少个元素可能是划分前选取的主元？

例如给定的排列是[1, 3, 2, 4, 5]。则：
1 的左边没有元素，右边的元素都比它大，所以它可能是主元；
尽管 3 的左边元素都比它小，但其右边的 2 比它小，所以它不能是主元；
尽管 2 的右边元素都比它大，但其左边的 3 比它大，所以它不能是主元；
类似原因，4 和 5 都可能是主元。
因此，有 3 个元素可能是主元。'''

#双循环遍历，可能超时
num = input()
numList = [int(i) for i in num.split(" ")]
def findMid(numList):
    midList = []
    totalMid = 0
    x = True
    y = True
    for i in numList:
        left = [j for j in numList if numList.index(j) < numList.index(i)]
        right = [k for k in numList if numList.index(k) > numList.index(i)]
        for j in left:
            if j > i:
                x = False
                break
            x = True
        for k in right:
            if k < i:
                y = False
                break
            y = True
        if x and y:
            totalMid += 1
            midList.append(i)
    return(totalMid, midList)
print(findMid(numList))

#单循环遍历
def findMid(numList):
    leftOk = []
    leftMax = 0
    for i in numList:
        if i > leftMax:
            leftOk.append(i)
            leftMax = i
    rightOk = []
    rightMin = float('inf')
    for index in range(len(numList) - 1, -1, -1):
        # 从右向左扫描整个列表
        if numList[index] < rightMin:
            rightOk.append(numList[index])
            rightMin = numList[index]

    answer = []
    for x in leftOk:
        if x in rightOk:
            answer.append(x)
            
    return(len(answer), " ".join([str(x) for x in answer]))
    

print(findMid(numList))

#位置不变
def findMid(numList):
    midList = []
    totalMid = 0
    sortNumList = sorted(numList)
    for i,j in zip(sortNumList, numList):
        if i == j:
            totalMid += 1 
            midList.append(i)
    return(totalMid,midList)
print(findMid(numList))
    
'''现在有同一个产品的N个版本，编号为从1至N的整数；其中从某个版本之后所有版本均已损坏。
现给定一个函数isBadVersion，输入数字N可判断该版本是否损坏（若损坏将输出True）；请找
出第一个损坏的版本。
注：有时isBadVersion函数运行速度很慢，请注意优化查找方式'''  

N = int(input())
isBadVersion = eval(input())
 
def firstBadVersion(N):
    left = 0
    right = N
    while right - left > 1:
        mid = left + (right-left)//2
        if isBadVersion(mid) == True:
            right = mid
        else:
            left = mid
    return right
       
       
print(firstBadVersion(N))






















            
            
    