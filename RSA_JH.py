# -*- coding: utf-8 -*-
print("----------------------------------------------------------")
print("--------------------INICIO DEL PROGRAMA-------------------")
print("-----------------------R---S---A--------------------------")
print("----------------------------------------------------------")
p=17
q=29
n=p*q
f_n=(p-1)*(q-1)
e=97 #Clave publica
e_i=e
#--------------------------------------
dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
     'l':12,'m':13,'n':14,'ñ':15,'o':16,'p':17,'q':18,'r':19,'s':20,'t':21,'u':22,
     'v':23,'w':24,'x':25,'y':26,'z':27}
valores=list(dic.values())
letras=list(dic.keys())

palabra=input("Ingrese la palabra: ")
palabra = palabra.lower()
print("--------------")
lista = list(palabra)
print("La palabra a cifrar es --> ", *lista, sep=" ")


print("--------------")

#Para cifrar la palabra
for i in range(len(lista)):
    if lista[i] in dic:
        lista[i] = dic[lista[i]]
    if isinstance(lista[i],int):
        lista[i]=(lista[i]**e_i)%n
         
print("El cifrado de la palabra es:")
print(*lista, sep=" - ")
print("--------------")

opcion = input("¿Desea descifrar la frase: ? ")
opcion = opcion.lower()
if opcion == "si":
    #-------------Euclides extendido--------------
    a= f_n
    b=e
    inv=[]
    if b == 0:
        print(0,1,0)       
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
            inv.append(v0)
    print("--------------")
    d=inv.pop()
    print("El inverso multiplicativo de e es:", d)    
    print("--------------")
#---------------------------------------------------------
    for i in range(len(lista)):
        if isinstance(lista[i],int):
            lista[i]=(lista[i]**d)%n
    print("La palabra descifrada en numeros es: ")        
    print(*lista, sep=" - ")       
    print("--------------")

    for i in range(len(lista)): 
        if lista[i] in valores:
            lista[i]=letras[lista[i]-1]
    print("La palabra descifrada es--> ", *lista, sep="")    
    print("--------------")
    print("Fin del programa")
    print("---------------------------------------------------------")
else: 
    print("Fin del programa")
    print("---------------------------------------------------------")


        