# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:09:09 2022

@author: elect
"""

students = ['manu','geetha','naman','diya','john']
#to print first item from this list
print(students[0])
#to print last item from this list
print(students[-1])
#to print second last item
print(students[-2])
#slicing method 
print(students[0:2])
#to print the entier list
print(students)
#to replace value
students[2]='manyan'
print(students)
#append function
students.append('sithara')
print(students)
#insert function
students.insert(1, 'deepak')
print(students)
#remove 
students.remove('john')
print(students)
students.pop(4)
print(students)
#sorting the list
students.sort()
print(students)
#decending order sorting
students.sort(reverse=True)
print(students)
#extend method
list2=['syam','devika','ammu']
students.extend(list2)
print(students)