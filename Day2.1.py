# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:44:09 2020

@author: AE401
"""

import random
ans=random.randint(1,20)
t=0
time=0
while t<=5:
    num=input("Please enter a number between 1~20:\n") 
    num=int(num)
    if num>=1 and 20>=num:
        if num<ans:
            print("Larger!!!")
            time=time+1
        elif num>ans:
            print("Smaller!!!You can only answer the smaller number FIVE time!!!")
            t=t+1
            time=time+1
        else:
            print("You are correct!")
            print("You've answered",time,"times!" )
            break
    else:   
        print("The number must between 1~20.")
        time=time+1