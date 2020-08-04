# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:36:32 2020

@author: AE401
"""

import random
ans=random.randint(1,20)
while True:
    num=input("Please enter a number between 1~20:\n") 
    num=int(num)
    if num>=1 and 20>=num:
        if num<ans:
            print("Larger!!!")
        elif num>ans:
            print("Smaller!!!")
        else:
            print("You are correct!")
            break
    else:   
        print("The number must between 1~20.")