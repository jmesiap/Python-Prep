#!/usr/bin/env python
# coding: utf-8

# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:<br>
# Color<br>
# Si es moto, auto, camioneta ó camión<br>
# Cilindrada del motor

# In[1]:

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:<br>
# Acelerar<br>
# Frenar<br>
# Doblar<br>

# In[5]:

class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
    
    def Acelerar(self, velocidad):
        print("la velocidad es de:", velocidad)

    def Frenar(self, velocidad):
        print("La distancia de frenado a una velocidad de",velocidad, "km/h es de:", round(velocidad*(velocidad/180),1), "mt")

    def Doblar(self, lado):    
        print("Voltear al lado:", lado)



# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado

# In[6]:

Veh_1 = Vehiculo("Verde", "Auto", 5)
Veh_2 = Vehiculo("Amarillo", "Moto", 3)
Veh_3 = Vehiculo("Cian", "Auto", 2)
Veh_1.Acelerar(100)  
Veh_2.Frenar(100)      
Veh_3.Doblar("Derecho")



# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada

# In[12]:


class Vehiculo:
    def __init__(self, color, tipo, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.velocidad = 0
        self.direccion = ""

    def Acelerar(self, velocidad):
        print("la velocidad es de:", velocidad)

    def Frenar(self, velocidad):
        print("La distancia de frenado a una velocidad de",velocidad, "km/h es de:", round(velocidad*(velocidad/180),1), "mt")

    def Doblar(self, lado):    
        print("Voltear al lado:", lado)

    def estado(self, velocidad, direccion):
        print("Estado del auto:", "Velocidad:", velocidad,"km/h",  "Dirección:", direccion)
    
    def detalle(self):
        print("Color:", self.color)
        print("Tipo:", self.tipo)    
        print("Cilindrada:", self.cilindrada)



# In[13]:






# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 7<br>
# Verificar Primo<br>
# Valor modal<br>
# Conversión grados<br>
# Factorial<br>

# In[33]:

class Func_creadas_Mod7:
    
    """ def __init__(self) -> None:
        pass """

    def F_primo(self, num):
        if num == 1: return False, num, "No es número primo"    

        for i in range(2,num):
            if  num % i == 0: 
                return False,num, "No es número primo"    
                break           
        return True, num, "Es número primo"    
    
    
    def F_Repite(self, numeros):
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
        


    def convertir(self, valor, origen, destino):
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
   
            return resultado, valor

  
    def Calc_facto(self, num):
        
        if num == 1:
            return 1
        if type(num) != int:
            return 'Debe ingresar un número entero'
        if num < 0:
            return 'El número debe ser positivo'
            
        num = num  * self.Calc_facto(num - 1)
        return num
        




# 6) Probar las funciones incorporadas en la clase del punto 5

# In[28]:

Func_C = Func_creadas_Mod7()

print ("-----------------Números primos-----------------")
print ("")
print(Func_C.F_primo(1))
print ("")
print("----------El número que mas se repite-----------")
print ("")
List_1, veces, num = Func_C.F_Repite([1,9,1,9,9,9,9,8,8,9,5,5,5,5,5,5,1,4,9,3])
for i in List_1:
   print(i)
print("El número ", num, "se repites : ", veces, " veces" )
print ("")

print("--------------Conversión de grados:--------------")
print ("")
Valor_Result, valo = Func_C.convertir(5, "Celsius", "Farenheit")    
print(valo,"Celcius convertido a Farenheit es igual a:",  round(Valor_Result,2))   
print ("")

print("-------------------Factorial:--------------------")
print ("")
print(Func_C.Calc_facto(6))



# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# In[55]:

class Func_creadas_Mod7:
    
    def __init__(self, Lista_Valores):
        self.Lista = Lista_Valores 


    def Calc_Primo(self):
        for i in self.Lista:
            print(self.F_primo(i))
            
    def F_primo(self, num):
        if num == 1: return num, "No es número primo"    

        for i in range(2,num):
            if  num % i == 0: 
                return num, "No es número primo"
                break           
        return  num, "Es número primo"    
    
   
    def F_Repite(self):
        self.Lista.sort()
        contador = 1
        mayor_Veces=0
        mayor_Num=0
        i = 1
        Lista_Nueva=[]
        while i < (len(self.Lista)):
            if self.Lista[i-1] == self.Lista[i]:
               contador = contador+1
               if i == len(self.Lista)-1:
                  Lista_Nueva.append([self.Lista[i-1], contador])  
                    
                  if contador > mayor_Veces:
                    mayor_Veces = contador 
                    mayor_Num = self.Lista[i-1] 

            else:
                Lista_Nueva.append((self.Lista[i-1], contador))    
                
                if contador > mayor_Veces:
                    mayor_Veces = contador 
                    mayor_Num = self.Lista[i-1]
                contador=1
            i += 1
        
        return Lista_Nueva, mayor_Veces, mayor_Num
    
    def Calc_Convertir(self, origen, destino ):
        for i in self.Lista:    
                Valor_Result = self.F_convertir(i, origen, destino)    
                print(i,"Celcius convertido a Farenheit es igual a:",  round(Valor_Result,2))   

    def F_convertir(self, valor, origen, destino):
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
    
    def Calc_facto(self):
        for i in self.Lista:
            print("Factorial de", i, ": ", self.F_facto(i))

    def F_facto(self, num):
        
        if num == 1:
            return 1
        if type(num) != int:
            return 'Debe ingresar un número entero'
        if num < 0:
            return 'El número debe ser positivo'
            
        num = num  * self.F_facto(num - 1)
        return num


# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones

# In[1]:

from TareaM08 import *
Prueba_Import = FuncionesM08([1,1,2,5,8,8,9,11,15,16,16,16,18,20])

print ("-----------------Números primos-----------------")
print ("")
print(Prueba_Import.Calc_Primo())
print ("")

print("----------El número que mas se repite-----------")
print ("")
List_1, veces, num = Prueba_Import.F_Repite()
for i in List_1:
   print(i)
print("El número ", num, "se repites : ", veces, " veces" )
print ("")

print("--------------Conversión de grados:--------------")
print ("")
Prueba_Import.Calc_Convertir("Celsius", "Farenheit")    
print ("")

print("-------------------Factorial:--------------------")
print ("")
print(Prueba_Import.Calc_facto())


