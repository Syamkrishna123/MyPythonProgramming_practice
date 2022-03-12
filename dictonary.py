# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 07:31:23 2022

@author: syamk
"""

#dictonary
student={'name':'syam','course':'datascience','batch':2}
print(student)
student['name']
#to change a value
student['name']='raman'
print(student)
#to add an key value pair
student['month']='feb'
#pop() method
student.pop('course')
print(student)
#popitem method will remove last inserted item 
student.popitem()
print(student)
#del keyword removes specified key name
del student['batch']
print(student)