# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 12:12:27 2018

@author: aneesh
"""
n = int(input())
arr = ['']*n
arr = list(map(int, input().split(' ')))
dic = {}
#print(arr)
mean = float(sum(arr)/n)
print(mean)
arr.sort()
if (n-1)%2 == 0:
    print(arr[n//2])
else:
    x = (n-1)//2
    print(float((arr[x]+arr[x+1])/2))
s=set(arr)
for i in s:
    dic[i] = arr.count(i)
maxcount = max(dic.values())
mode = max(s,key=arr.count)
for key, value in dic.items():
    if value == maxcount:
        if key < mode:
            mode= key
print(mode)

    