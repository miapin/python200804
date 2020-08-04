# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:41:32 2020

@author: AE401
"""

highest=0
lowest=100
avg=0
total=0
scores=[]
n=input("How many people are there in your class?")
n=int(n)
for b in range(n):
    S=input("please enter the scores:")
    S=int(S)
    scores.append(S) 
for a in scores:
    total=total+a
avg=total/n
print("The total is",total)
print("The average is",avg)
for c in scores:
    if c>highest:
        highest=c
print(highest)