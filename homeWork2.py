#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:45:21 2020

@author: liwenxi
"""
class Node():
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev
        
class LinkStack():
    def __init__(self):
        self.head = None
        self.length = 0
    
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        return self.length
    
    def peek(self):
        return self.head.getData()
    
    def push(self,item):
        top = self.head
        self.head = Node(item)
        self.head.getNext = top
        self.length += 1
    
    def pop(self):
        top = self.head.getData()
        self.head = self.head.getNext
        self.length -= 1
        return top

class LinkQueue():
    # 请在此编写你的代码（可删除pass语句）
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def isEmpty(self):
        return self.head is None
    
    def size(self):
        return self.length
    
    def enqueue(self, item):
        if self.head is None:
            self.head = self.tail = Node(item)
        else:
            top = self.head
            self.head = Node(item)
            self.head.getNext = top
        self.length += 1
    
    def dequeue(self):
        item = self.tail.getData()
        if self.tail == self.head :
            self.tail = self.head = None
        else:
            self.tail = self.tail.getPrev()
        self.length -= 1
        return item
        
            
    # 代码结束


# 检验
print("======== 4-Link Stack & Link Queue ========")
s = LinkStack()
q = LinkQueue()
for i in range(10):
    s.push(i)
    q.enqueue(i)
print(s.peek(), q.dequeue())  # 9 0
print(s.pop(), q.size())  # 9 9
while not s.isEmpty():
    s.pop()
print(s.size(), q.isEmpty())  # 0 False



        
        
    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    