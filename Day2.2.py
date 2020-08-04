# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:16:19 2020

@author: AE401
"""

while True:
    x=input("Please enter a number:")
    x=int(x)
    if x==1 or x==0:
        print("此不為質數")
    elif x%2!=0 or x==2 or x%3!=0 or x==3 or x%5!==0 or x=5 :
        print("此為質數")
    else:
        print("此不為質數")
    