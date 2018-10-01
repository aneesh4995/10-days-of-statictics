
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:37:35 2018

@author: aneesh
"""
n = int(input())
arr=['']*n
arr = list(map(int , input().split(' ')))
from statistics import median
g = n//2
arr.sort()
if (n-1)%2 == 0:
    x = n//2
    q2=arr[x]
else:
    x = (n-1)//2
    q2=int((arr[x]+arr[x+1])/2)

qur1 = arr[:g]
qur3 = arr[x+1:]
q1=int(median(qur1))
q3=int(median(qur3))
print(q3-q1)