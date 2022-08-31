# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:57:35 2022

@author: juans
"""
try: 
    expo=[]
    axa=[]
    post = 0
    y = 1
    
    a= int(input("Ingrese una variable (Entera): "))
    e= int(input("Ingrese el exponente: "))
    e_1=e
    list = [e%2]
    while e!=0:
        e = int(e/2)
        aux = e%2
        list.append(aux)
        
    list.reverse()
    list.remove(0)

    print(f"{e_1}_binario= ", *list, sep = " ")
    list.reverse()
    
    for i in list:
        
        if i == 1:
            expo.append(post)
        else:
            expo.append(0)
        post +=1
        
    
    for i in range(len(expo)):
        axa.append(a)
        a=a*a
    post = 0
    for i in range(len(expo)):
        if expo[i]!= 0:
            y *= axa[i]
            
        
    print(y)
except:
    
    print("Se digito una variable de manera erronea")
    