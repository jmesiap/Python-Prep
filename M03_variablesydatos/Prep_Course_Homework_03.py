#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

num=1
print (num)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(num))



# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_Nombre="José Ivan Mesia Portocarrero"


# 5) Crear una variable que contenga un número complejo

# In[3]:


num_Complejo = 5 + 5j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(num_Complejo))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


valor_PI=round(3.14159265359,4)
print(valor_PI)


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

valor_True1 = "True"
valor_True2 = True
# no se trata de lo mismo, son tipos de dato distinto str y boolean respectivamente


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(valor_True1))
print(type(valor_True2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 5 + 5.8



# 11) Realizar una operación de suma de números complejos

# In[2]:

a = 5 + 5j
b = 8 + 8j
z = a + b
print(z)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

a = 5j+3.5 



# 13) Realizar una operación de multiplicación

# In[5]:


print (5 * 3)


# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

x = (27 / 4)
print(x)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

y = (27 // 4)
print(y)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

x = (27 % 4)
print(x)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

print(y*4+x)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

print("Hola" + " Pepe," + " tu edad es", 44)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print("2" == 2 )
# La respuesta es False, debido a que son tipos de dato distintos, str y int respectivamente


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(int("2") == 2 )



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

# El error es debido a que no se puede covertir texto a numero, en este caso la coma "," 


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

a = 3
a -= 1
print(a)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print (1 << 2)
# Sistema binario, el numero 1 se desplaza 2 pisiciones a la izquierda, las posiciones desplazadas se completan con ceros "0",
# de esta forma pasa de 0001 a 0100 que es el numero 4 en el sistema decimal 


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

# print(2 + "2") no esta permitido por que son distintos tipo de dato
# si fueran del mismo tipo de dato si da siempre el mismo resultado, ejemplo:
print (int(2) + int("2"))
# ó
print (str(2) + "2")

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

print(2 + int("2"))

