# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

f=open("/Users/liwenxi/Downloads/Austen_Emma.txt","r")
myFile=f.read()
f.close
#将读取进来的文件按空格切成词
myList=myFile.split(" ")
#将所有词及其频数写进词典
myDict={}
for i in myList:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] = myDict[i] + 1
#对字典按照首字母的顺序进行排列
sortedDict1=sorted(myDict)
#对字典按照出现频数的大小顺序进行排列
sortedDict2=sorted(myDict.items(),key=lambda x:x[1],reverse=True)
#对字典按照尾字母的次序进行排列
sortedDict3={}
#对字典里的键按照尾字母排序
sortedListOfKeys=sorted(myDict.keys(),key=lambda x:x[-1],reverse=False)
#对排序好的键列表进行赋值
for w in sortedListOfKeys:
    for word in myDict:
        if w==word:
            sortedDict3[w]=myDict.get(word)
print(sortedDict3)
