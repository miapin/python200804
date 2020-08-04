# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:54:10 2020

@author: AE401
"""

import random
ans=random.randint(1,10)
num=input("Please enter a number between 1~10:\n") 
num=int(num)
if num>=1 and 10>=num :
    if num==ans:
        print("You are corret!")
    else:
        print("Sorry, you are wrong!")
else:
    print("The number must between 1~10")