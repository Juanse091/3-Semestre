# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 19:59:20 2022

@author: juans
"""

def xgcd(a, b):
    if b == 0:
        return 0,1,0
 
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
 
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1

        a = b
        b = r

        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
 
    return  a, u0, v0


a = int(input("Dado el número a: "))
b = int(input(" Y el B: "))

print(xgcd(a,b))