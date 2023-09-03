#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
num = 8
if (num > 0):
    print("es mayor a cero")
elif (num < 0) :  
    print("es menor a cero")    
else: 
    print("es igual a cero")




# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 5
b = 8

if (type(a)==type(b)):
   print("Son el mismo tipo de dato: ", type(a)) 
else: 
   print("Son distintos tipos de dato: ")    



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:
for i in range(1, 21):
    if (i%2 == 0):
        print (i, ": es par")
    else:
        print (i, ": es impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for num in range(6):
    print(num, " a la potencia de 3 es = ", num**3)



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

num=5
for i in range(1,num+1):
    print(i)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:

numero = 3
varNum = numero
facto = 1
if (numero > 0):
    while (numero > 0):
        facto = facto * numero
        numero = numero - 1
else:
    facto = 1            
print ("Factorial de ", varNum, " = ", facto)



# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

num = 5
x = 1
while (num > 0):
    print("Ciclo while numero: ", (num-num+x))
    for i in range(1, num+1):
        print("    Ciclo for numero: ", i)
    num = num - 1
    x = x + 1    



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:

xxx = 3

for i in range(1, xxx+1):
    yyy = 3    
    print('Ciclo for nro ', i)
    
    while(yyy > 0):
        print('     Ciclo while nro ' , yyy)
        
        yyy = yyy - 1
        



# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:
Num_Primo = 30
Acum_P = 0
num = 2

while (num <= (Num_Primo)):

    for i in range(2, num+1):
       if (num % i == 0):
          Acum_P = Acum_P + 1

    if (Acum_P == 1):
       print(num, " = Es numero primo!")

    Acum_P = 0
    num = num + 1 



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:

Num_Primo = 30
Acum_P = 0
num = 2

while (num <= (Num_Primo)):

    for i in range(2, num+1):
       if (num % i == 0):
          Acum_P = Acum_P + 1
          
          if Acum_P > 1: break

    if (Acum_P == 1):
       print(num, " = Es numero primo!")

    Acum_P = 0
    num = num + 1 



# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

Num_Primo = 30
Acum_P = 0
num = 2
acum_sin_break = 0
while (num <= Num_Primo):

    for i in range(2, num+1):
       acum_sin_break = acum_sin_break + 1 
       if (num % i == 0):
          Acum_P = Acum_P + 1

    if (Acum_P == 1):
       print(num, " = Es numero primo!")

    Acum_P = 0
    num = num + 1 

print ("El numero de iteracciones  = ", acum_sin_break)


# In[57]:

Num_Primo = 30
Acum_P = 0
num = 2
acum_con_break = 0
while (num <= Num_Primo):

    for i in range(2, num+1):
       acum_con_break = acum_con_break + 1 
       if (num % i == 0):
          Acum_P = Acum_P + 1
          if Acum_P > 1: break

    if (Acum_P == 1):
       print(num, " = Es numero primo!")

    Acum_P = 0
    num = num + 1 

print ("El numero de iteracciones  = ", acum_con_break)

print('Se optimizó a un ' + str(int((acum_con_break/acum_sin_break)*100)) + '% de ciclos aplicando break')


# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

numeros = 100
while(numeros <= 300):
    if (numeros % 12 != 0):
       numeros = numeros + 1
       continue
    print(numeros)
    numeros = numeros + 1



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
rpta="si"
while rpta == "si": 
   rpta = str(input("Desea ingresar un número y saber si es primo?: "))
   if rpta == "si":      
      Num_Primo = int(input("Ingresa un numero entero mayor a 1: "))
      acum = 0
      num = 2

      while (num <= (Num_Primo )):

         for i in range(2, num+1):
            if (num % i == 0):
               acum = acum + 1

         if (acum == 1):
            print(num, " = Es numero primo!")

         acum = 0
         num = num + 1 
   else:
      break   

# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:


n = 100
while(n<=300):
    if (n % 3 == 0):
        print('El número es: ', str(n))
        break
    n += 1
