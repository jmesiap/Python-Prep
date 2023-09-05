#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
Mi_Lista = list()

num = (-15)
while True:
    if num > (-1): break
    Mi_Lista.append(num)
    num +=1
print(Mi_Lista)




# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
i = 0
while len(Mi_Lista)>i:
    if Mi_Lista[i] % 2 == 0:
        print(Mi_Lista[i])
    i = i + 1





# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for i in range(len(Mi_Lista)):
    if Mi_Lista[i] % 2 == 0:
        print(Mi_Lista[i])



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:

i=0
for c in Mi_Lista:
    if i>2: break
    i +=1
    print(c)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
for i, c in enumerate(Mi_Lista):
    if i>2: break
    print(i, c)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

Nueva_Lista=[1,2,5,7,8,10,13,14,15,17,20]
for idx, val in enumerate(Nueva_Lista):
    if idx+1 != val:
       Nueva_Lista.insert(idx, idx+1) 
print(Nueva_Lista)



# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:

S_Fibo=[0,1]
print (S_Fibo)
for i in range(28):
    S_Fibo.append(S_Fibo[i+1]+S_Fibo[i])

print(S_Fibo)



# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print(sum(S_Fibo))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

print(S_Fibo)
conta = len(S_Fibo)-1
x=0
for i in range(1, 6):
    print((S_Fibo[conta-x])/(S_Fibo[conta-i]))
    conta = conta - 1
    x=x+1


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:


cadena = "Hola Mundo. Esto es una practica del lenguaje de programación Python"
for pos, val in enumerate(cadena):
    if val=="n":
        print("n esta en la posición: ", pos)


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

Mi_Diccionario = {
    "Código": ["C001", "C002", "C003"],
    "Nombres": ["José", "Mateo", "Janet"],
    "Apellidos": ["Mesia", "Mesia Díaz", "Vargas"],
    "Edad": [44, 5, 44]
}

for clave in enumerate(Mi_Diccionario.keys()):
    print( clave)



# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:

Lista_Cadena = list(cadena)
for val in enumerate(Lista_Cadena):
    print(val)



# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]

U_Listas = zip(lista_1, lista_2)

for elem  in U_Listas:
    print (elem)



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
condi = False
for numero in lis:
    if numero % 7 == 0:
        if condi==False:
           Nueva_lis = list ()
           Nueva_lis.append(numero)
           condi=True
        else:
          Nueva_lis.append(numero)

print(Nueva_lis)   



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis=[[1,2,3,4], "rojo", "verde", [True, False, False],["uno", "dos", "tres"]]
cantidad = 0
for elem in lis:
    if type(elem)== list:    
       cantidad = cantidad + len(elem)
    else: 
        cantidad +=1   

print(cantidad)


# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

for i, elem in enumerate(lis):
    if type(elem) != list:
       lis[i] = [elem]

print (lis)


# %%
