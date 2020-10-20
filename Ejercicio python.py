#!/usr/bin/env python
# coding: utf-8

# Ejercicio 1:
# Realiza una variable con tu matricula y realiza una secuencia de imprimir con tu nombre y tu matricula concatenados.

# In[3]:


x="Miguel Alejandro Noriega Ortega"
y="#1798528"
print(x,y)


# Ejercicio 2:
# Pidiendo el input del usuario pide dos números y crea una pequeña calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.
# 

# In[5]:


a1 = int(input("Introduce un número:" ))
b1 = int(input("Introduce otro número: "))
s=a1+b1
r=a1-b1
m=a1*b1
d=a1/b1
e=a1**b1
print("La suma de los numeros es",s)
print("La resta de los numeros es",r)
print("La multiplicacion de los numeros es",m)
print("La division de los numeros es",d)
print("La exponencial de los numeros es",e)


# Ejercicio 3:
# Con loop while o for, realiza una lista de 10 numeros multiplos de 3, y después realiza una función de loop que sume todos los números dentro del arreglo.

# In[25]:


lista=list()
for i in range(1,11):
   lista.append(i*3)
print("Los numeros en la lista son: ",lista)
suma=sum(lista)
print("La suma de los numeros en la lista es:",suma)


# Ejercicio 4
# Con una función de if else, revisar si un número es par o es impar.
# Con una función de if else, revisar si un número es primo o no.

# In[60]:


n = int(input("Introduce un número:" ))
r= n%2
if (r==0):
    print("El numero es par")
else:
    print ("El numero es impar")
    
for i in range(2,n): #codigo de https://www.youtube.com/watch?v=SpTAxH_Geow&ab_channel=Telusko
        if n % i ==0:
            print("El numero no es primo")
            break
else:
    print("El numero es primo ")


# Ejercicio 5
# Utilizando diferentes clases en python, crea una calculadora con los operadores básicos de suma, resta, multiplicación, división, y exponente.

# In[64]:


def Suma(a,b):
    c=a+b
    return c
def Mult(a,b):
    d=a*b
    return d
def Rest(a,b):
    e=a-b
    return e
def Div(a,b):
    f=a/b
    return f
def Exp(a,b):
    g=a**b
    return g

a1 = int(input("Introduce un número:" ))
b1 = int(input("Introduce otro número: "))

print ("Suma numeros -->", Suma(a1,b1))
print ("Resta de numeros -->", Rest(a1,b1))
print ("Multiplicacion de numeros -->", Mult(a1,b1))
print ("Division de numeros -->", Div(a1,b1))
print ("Exponencial de numeros -->", Exp(a1,b1))


# # Tuplas

# Crear una variable flotante, integer, boleana y compleja e imprimir el tipo de variable que es.

# In[73]:


z=1
v=2.5
t=2<1
u = 1+2j
print("z es una variable tipo: ",type(z))
print("v es una variable tipo: ",type(v))
print("t es una variable tipo: ",type(t))
print("u es una variable tipo: ",type(u))


# Crear una tupla con valores enteros imprimir el primer y ultimo valor.
# 
# 

# In[88]:


b=(1,2,3,4,5)
print(b[0],b[4])


# Añadir 3 valores de string a la tupla.

# In[89]:


b=b+("hola","adios","saludos")
print(b)


# Verificar si una variable existe dentro de la tupla.
# 
# 

# In[94]:


print( 2 in b)


# # Listas

# Crear una lista con 40 elementos aleatorios enteros.
# 
# 

# In[109]:


import random as r
my_list=[]
for i in range(1,40):
    my_list=[r.randint(1, 100)]
    print(my_list)


# Con una funcion (def) crear dos listas nuevas a partir de la lista creada por numeros aleatorios, en la cual en una esten los elementos pares, y en la otra los elementos impares.

# In[256]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
par=[]
for i in lis:
    if i % 2 == 0:
        par.append(i)

print(par)

 


# In[257]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
impar=[]
for i in lis:
    if i % 2 != 0:
        impar.append(i)

print(impar)


# Crear dos variables con la longitud de ambas listas nuevas e imprimir las variables.

# In[241]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
par=[]
for i in lis:
    if i % 2 == 0:
        par.append(i)
p=len(par)
print(p)


# In[243]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
impar=[]
for i in lis:
    if i % 2 != 0:
        impar.append(i)

ip=len(impar)
print(ip)


# Ordenar los elementos de la lista par de mayor a menor, y los de la lista impar de menor a mayor.

# In[244]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
par=[]
for i in lis:
    if i % 2 == 0:
        par.append(i)
par.sort()
print(par)


# In[246]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
impar=[]
for i in lis:
    if i % 2 != 0:
        impar.append(i)

impar.sort(reverse=True)
print(impar)


# Utilizar al menos cuatro de las funciones de listas en python en la lista original de 40 elementos.

# In[275]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
print(min(lis))


# In[267]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
lis.reverse
print(lis)


# In[268]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
lis.insert(2,3)
print(lis)


# In[273]:


lis=[8,48,74,17,78,13,73,76,82,44,20,79,40,10,49,32,64,77,48,99,3,85,70,17,68,49,39,33,71,15,96,38,49,88,9,23,57,38,39]
print(max(lis))


# # Diccionarios

# Crear un diccionario de 6 personas que conozcas con su primer nombre y su edad.
# 
# 

# In[317]:


names=('Mariana','Luis','Jessica','Blanca','Alejandro','Tania')


# In[311]:


dict = {'Name1': 'Mariana', 'Age1': 17,'Name2': 'luis', 'Age2': 55,'Name3': 'jessica', 'Age3': 20,
        'Name4': 'Blanca', 'Age4': 57, 'Name5': 'Alejandro', 'Age5': 20,'Name6': 'Tania', 'Age6': 23,  }
#https://stackabuse.com/python-dictionary-tutorial/#:~:text=To%20create%20a%20Python%20dictionary,the%20keys%20must%20remain%20unique.


# Crear una lista con los valores de la edad y reacomodar la lista de menor a mayor valor.
# 
# 
# 

# In[313]:


edades=[dict["Age1"],dict["Age2"],dict["Age3"],dict["Age4"],dict["Age5"],dict["Age6"]]
edades.sort()
print(edades)


# Usando el diccionario y un loop, imprimir solo los nombres.
# 
# 

# In[318]:


for i in names :
    print(i)


# Añadir dos personas nuevas a tu diccionario, incluyendo edad.
# 
# 

# In[320]:


dict['Paola']=24
dict['Nadia']=27
print(dict)


# # Sets

# Crea un set con 100 numeros aleatorios enteros del 1 al 25.
# 
# 

# In[322]:


import random as r
set={}
for i in range(0,100):
    set={r.randint(1, 25)}
    print(set)


# In[331]:


set={23,2,9,22,18,17,25,23,5,6,3,10,10,4,11,4,2,5,9,17,
     3,16,12,13,11,18,7,7,9,2,16,8,6,6,10,10,5,10,22,3,
     17,15,7,17,3,10,24,16,2,2,5,24,15,24,19,15,13,10,14
     ,10,15,7,9,10,15,17,14,7,7,1,1,4,18,5,6,11,2,10,19,2,
     14,11,12,4,18,16,2,14,6,15,8,23,5,13,14,12,11,23,24,13}
set


# Comprueba la longitud de tu set.
# 
# 

# In[332]:


len(set)


# Crea una lista de 5 numeros aleatorios del 1 al 10 y comprueba si cada valor aparece en el set inicial.
# 
# 

# In[336]:


import random as r
l=list()
for i in range(0,5):
    l=[r.randint(1, 10)]
    print(l)


# In[339]:


l=(3,2,5,5,9)
set.intersection( l )

print("Los numeros que las listas tienen en comun son:",set.intersection( l ))


# In[ ]:




