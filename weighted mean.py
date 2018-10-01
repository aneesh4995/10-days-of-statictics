
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 10:48:51 2018

@author: aneesh
"""
n = int(input())
val = ['']*n
wei = ['']*n
val = list(map(int , input().split(' ')))
wei = list(map(int , input().split(' ')))
nom = 0 
for i in range(len(val)):
    nom = nom + val[i]*wei[i]
print(round(nom/sum(wei),1))