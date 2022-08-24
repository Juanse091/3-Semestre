# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 20:14:57 2022

@author: juans
"""

#Variables
expo= -1
Otherlist = []
c= 0
x = 0

#PROGRAMA
n = int(input("Ingrese un valor= "))
print(n+"^1000")

list = [n%2]
while n!=0:
    n = int(n/2)
    aux = n%2
    list.append(aux)
    
list.reverse()
list.remove(0)

print(*list, sep = " ")
list.reverse()

for i in list:
    expo +=1
    
    if i == 1:
        x= 2**expo
        c=x + c
        
    
    

print(c)