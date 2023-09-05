#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
Lista_Ciudades = ["Nueva York", "Londres", "Tokio", "París", "Dubai", "Sídney", "Hong Kong", "Singapur", "Seúl" , "San Petersburgo"]
print(Lista_Ciudades)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print("El segundo elemento es: ",Lista_Ciudades[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print("Del segundo al cuarto elemento, son : ",Lista_Ciudades[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:


print("El tipo de dato de la lista es: ",type(Lista_Ciudades))


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

print(Lista_Ciudades[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:


print(Lista_Ciudades[:4])
    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:


Lista_Ciudades.append("Dubai")
Lista_Ciudades.append("Rioja")
print(Lista_Ciudades)

# No ocurre ningun error






# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

Lista_Ciudades.insert(3,"Moyobamba")
print(Lista_Ciudades)



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

Lista_Ciudades.extend(["Posic", "Nueva Cajamarca"])
print(Lista_Ciudades)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

Lista_Ciudades.index("Dubai") 
# la unica particularidad es que la posición de la ciudad buscada "Dubai" es la numero 6 pero su indice indica el numero 5, es decir las listas tienen 
# como primera posición el numero cero "0"



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

Lista_Ciudades.index("Tarapoto")
# Muestra un error, debido a que ese elemento no esta en la lista



# 12) Eliminar un elemento de la lista

# In[25]:

print(Lista_Ciudades)
Lista_Ciudades.remove("Dubai")
print(Lista_Ciudades)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:


Lista_Ciudades.remove("Tangamandapio")
# Muestra un error, debido a que ese elemento no esta en la lista


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

Ultimo_Elemento = Lista_Ciudades.pop()
print(Ultimo_Elemento)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(Lista_Ciudades * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

Tupla_Numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
print(Tupla_Numeros)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(Tupla_Numeros[10:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

print(20 in Tupla_Numeros)
print(30 in Tupla_Numeros)



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

Ciudad_a_Agregar = "Soritor"
varL = Ciudad_a_Agregar in Lista_Ciudades 
if varL == False:
   Lista_Ciudades.append(Ciudad_a_Agregar)
   print("Se agrego correctamente")
else:
   print("Ciudad ya existe")
print(Lista_Ciudades)



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print(Tupla_Numeros.count(5))
print(Lista_Ciudades.count("Tangamandapio"))



# 21) Convertir la tupla en una lista

# In[52]:

Tupla_a_Lista = list(Tupla_Numeros)
print(Tupla_a_Lista, type(Tupla_a_Lista))



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


a, b, c, *_ = Tupla_Numeros
print (a, b, c)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:


Dicci_Ciudades = {
    "Ciudad": Lista_Ciudades,
    "Pais": None,
    "Continente": None,
}
print(Dicci_Ciudades)



# 24) Imprimir las claves del diccionario

# In[59]:

print(Dicci_Ciudades.keys())


# 25) Imprimir las ciudades a través de su clave

# In[61]:
print(Dicci_Ciudades["Ciudad"])



