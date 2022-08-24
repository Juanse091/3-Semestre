# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:04:11 2022

@author: juans
"""




num = int(input("Ingrese el número que desea transformar: "))
base = int(input("Ingrese la base a la que lo quiere convertir (Debe ser mayor a 1): "))

mod=[num%base]

while num!=0:
    num = int(num/base)
    aux = num%base
    mod.append(aux)
    

mod.reverse()
mod.remove(0)
print(*mod, sep = " ")

