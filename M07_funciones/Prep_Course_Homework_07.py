#!/usr/bin/env python
# coding: utf-8

# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es

# In[1]:


def F_primo(num):
    
    if num == 1: return False

    for i in range(2,num):
        if  num % i == 0: 
            return False
            break           
    return True        
    
print(F_primo(6))


# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista

# In[25]:

def F_List_Primo(lista_Num):
    Nueva_lista=list()
    for i in lista_Num:
        indi = F_primo(i) 
        if indi==True:
            Nueva_lista.append(i)
    
    return Nueva_lista

Mostrar = F_List_Primo([1, 2, 3, 4, 5, 6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])    
print(Mostrar)


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera

# In[33]:


def F_Repite(numeros):
    numeros.sort()
    contador = 1
    mayor_Veces=0
    mayor_Num=0
    i = 1
    Lista_Nueva=[]
    while i < (len(numeros)):
        if numeros[i-1] == numeros[i]:
           contador = contador+1
           if i == len(numeros)-1:
              Lista_Nueva.append([numeros[i-1], contador])  
                   
              if contador > mayor_Veces:
                 mayor_Veces = contador 
                 mayor_Num = numeros[i-1] 

        else:
            Lista_Nueva.append((numeros[i-1], contador))    
            
            if contador > mayor_Veces:
               mayor_Veces = contador 
               mayor_Num = numeros[i-1]
            contador=1
        i += 1
    
    return Lista_Nueva, mayor_Veces, mayor_Num
    

List_1, veces, num = (F_Repite([1,9,1,5,5,5,5,5,5,1,4,9,3]))
for i in List_1:
   print(i)

print("El número ", num, "se repites : ", veces, " veces" )


# 4) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# 

# In[56]:

def convertir(valor, origen, destino):
    resultado=0
    if origen=="Celsius":
        if destino == "Farenheit":
            resultado = (valor*1.8) + 32    
        elif destino == "Kelvin":
            resultado = valor + 273.15    
        elif destino == "Celsius":
            resultado = valor        
        else: print("Inghrese valor correcto Farenheit, Kelvin ó Celsius")
    elif origen=="Farenheit":
        if destino == "Celsius":
            resultado = (valor-32) + 1.8    
        elif destino == "Kelvin":
            resultado = ((5*valor) + 2298.35)/9
        elif destino == "Farenheit":
            resultado = valor        
        else: print("Inghrese valor correcto Farenheit, Kelvin ó Celsius")
    elif origen=="Kelvin":
        if destino == "Celsius":
            resultado = valor-273.15
        elif destino == "Farenheit":
            resultado = (9*valor-2458.35)/5 + 32
        elif destino == "Kelvin":
            resultado = valor        
        else: print("Inghrese valor correcto Farenheit, Kelvin ó Celsius")
    else: print("Inghrese valor correcto Farenheit, Kelvin ó Celsius")    
   
    return resultado

Valor_Result = convertir(5, "Celsius", "Farenheit")    

print(round(Valor_Result,2))

# 5) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:

# In[62]:
lista_valores=["Celsius", "Kelvin", "Farenheit"]
print("Ingrese un valor a convertir: ")
num = int(input ())

for i in range(3):
    for j in range(3):
        
        print (num,"grados",lista_valores[i], "es igual a: ",round(convertir(num, lista_valores[i], lista_valores[j])), "grados", lista_valores[j])



# 6) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo

# In[65]:

def Calc_facto(num):
    
    if num == 1:
        return 1
    if type(num) != int:
        return 'Debe ingresar un número entero'
    if num < 0:
        return 'El número debe ser positivo'
        
    num = num  * Calc_facto(num - 1)
    return num

print(Calc_facto(5.5))


