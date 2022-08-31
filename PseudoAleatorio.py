# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 20:38:31 2022

@author: juans
"""
list = []
x = int(input("Inicio: "))
a = int(input("Multiplicador: "))
c = int(input("Desface: "))
m = int(input("Modulo: "))
limit = int(input("Limite: "))

for i in range(0,limit):
    x = (a*x+c)%m
    list.append(x)
print(list)