# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:10:48 2022

@author: elect
"""

#to practice the string datatype
title="python programing"
print(len(title))
print(title.capitalize())
print(title.upper())
print(title.casefold())
print(title.center(2,'m'))
#replce function
txt='one and one are friends and one and two are mates'
x=txt.replace('one', 'three',2)
print(x)
#count function
p=[1,2,3,4,5,5,6,7,9,8,7,2]
print(p.count(2))

