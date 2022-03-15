# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 17:33:23 2022

@author: elect
"""

#if condition
i=int(input("enter the number:"))
if i%2==0:
    print('the number is even')
else:
    print('the number is odd')
    
#elif
k=input('enter the day:')
if k=='monday':
    print("the first day of school")
elif k=='sunday':
    print('happy holiday')
elif k=='saturday':
    print('weekend')
else:
    print('usual work day')